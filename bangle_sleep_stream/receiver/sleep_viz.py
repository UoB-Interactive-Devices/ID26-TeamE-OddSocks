"""Generate sleep-stream visualizations and nightly diagnostics.

This script reads SQLite sleep updates and produces:
- Per-night static PNG figures
- Per-night interactive HTML timeline
- Per-night metrics JSON/CSV
- Cross-night summary metrics and trend figures

It is designed for practical detector sanity checking when PSG is unavailable.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from withings_import import load_withings_hr, load_withings_nights_summary, load_withings_sleep


STAGE_ORDER = ["awake", "light", "deep", "rem"]
STAGE_ORDER_COLLAPSED = ["awake", "light", "deep"]
STAGE_COLORS = {
    "awake": "#e76f51",
    "light": "#2a9d8f",
    "deep": "#264653",
    "rem": "#e9c46a",
    "other": "#9aa0a6",
}
STAGE_FROM_CODE = {2: "awake", 3: "light", 4: "deep", 5: "rem"}
SOURCE_MODE_LABEL = {0: "movement", 1: "hrm"}
SOURCE_MODE_COLORS = {0: "#7f8c8d", 1: "#1d3557"}


def _collapse_stage(stage: object) -> Optional[str]:
    if stage is None or (isinstance(stage, float) and np.isnan(stage)):
        return None
    s = str(stage)
    return "light" if s == "rem" else s


@dataclass
class NightSummary:
    night_id: str
    session_id: int
    start_local: datetime
    end_local: datetime
    duration_min: float
    n_rows: int
    epoch_sec: float


def resolve_db_path(user_db: Optional[str]) -> Path:
    if user_db:
        return Path(user_db).expanduser().resolve()

    script = Path(__file__).resolve()
    candidates = [
        Path.cwd() / "sleepstream.db",
        script.parents[2] / "sleepstream.db",
        script.parents[1] / "sleepstream.db",
        script.parent / "sleepstream.db",
    ]
    for c in candidates:
        if c.exists():
            return c.resolve()
    return candidates[0].resolve()


def load_sleep_updates(db_path: Path, tz_mode: str) -> pd.DataFrame:
    uri = f"file:{db_path}?mode=ro"
    conn = sqlite3.connect(uri, uri=True, timeout=10)
    try:
        df = pd.read_sql_query(
            """
            SELECT
              id,
              recv_ts_ms,
              watch_ts_sec,
              sequence,
              status,
              consecutive,
              source_mode,
              movement,
              bpm,
              sdhr,
              peer
            FROM sleep_updates
            ORDER BY watch_ts_sec ASC, recv_ts_ms ASC, id ASC
            """,
            conn,
        )
    finally:
        conn.close()

    if df.empty:
        raise ValueError(f"No rows in sleep_updates: {db_path}")

    watch_dt = pd.to_datetime(df["watch_ts_sec"], unit="s", utc=True)
    recv_dt = pd.to_datetime(df["recv_ts_ms"], unit="ms", utc=True)
    if tz_mode == "local":
        local_tz = datetime.now().astimezone().tzinfo
        watch_dt = watch_dt.dt.tz_convert(local_tz).dt.tz_localize(None)
        recv_dt = recv_dt.dt.tz_convert(local_tz).dt.tz_localize(None)
    else:
        watch_dt = watch_dt.dt.tz_convert("UTC").dt.tz_localize(None)
        recv_dt = recv_dt.dt.tz_convert("UTC").dt.tz_localize(None)

    df["watch_dt"] = watch_dt
    df["recv_dt"] = recv_dt
    df["stage_label"] = df["status"].map(STAGE_FROM_CODE)
    df["source_mode_label"] = df["source_mode"].map(SOURCE_MODE_LABEL).fillna("unknown")
    df["lag_sec"] = (df["recv_ts_ms"] / 1000.0) - df["watch_ts_sec"]
    return df


def infer_epoch_seconds(watch_ts: pd.Series) -> float:
    d = watch_ts.diff()
    d = d[(d > 20) & (d < 300)]
    if d.empty:
        return 60.0
    return float(d.median())


def assign_sessions(df: pd.DataFrame, session_gap_min: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    out = df.sort_values(["watch_ts_sec", "recv_ts_ms", "id"]).copy()
    out["gap_sec"] = out["watch_ts_sec"].diff()
    out["new_session"] = out["gap_sec"].isna() | (out["gap_sec"] > session_gap_min * 60)
    out["session_id"] = out["new_session"].cumsum().astype(int)

    sessions = (
        out.groupby("session_id", as_index=False)
        .agg(
            start_ts=("watch_ts_sec", "min"),
            end_ts=("watch_ts_sec", "max"),
            start_local=("watch_dt", "min"),
            end_local=("watch_dt", "max"),
            n_rows=("id", "count"),
        )
        .sort_values("session_id")
    )
    sessions["duration_min"] = (sessions["end_ts"] - sessions["start_ts"]) / 60.0
    sessions["night_date"] = (sessions["start_local"] - pd.Timedelta(hours=12)).dt.date.astype(str)
    sessions["night_id"] = [f"{d}_s{sid:02d}" for d, sid in zip(sessions["night_date"], sessions["session_id"])]
    return out, sessions


def dedupe_for_analysis(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.sort_values(["watch_ts_sec", "recv_ts_ms", "id"])
        .drop_duplicates(subset=["watch_ts_sec"], keep="last")
        .reset_index(drop=True)
    )


def get_episodes(night_df: pd.DataFrame, epoch_sec: float) -> pd.DataFrame:
    ep = night_df.sort_values("watch_ts_sec").copy()
    ep["stage_for_ep"] = ep["stage_label"].fillna("other")
    ep["episode_change"] = ep["stage_for_ep"] != ep["stage_for_ep"].shift(1)
    ep["episode_id"] = ep["episode_change"].cumsum().astype(int)

    out = (
        ep.groupby("episode_id", as_index=False)
        .agg(
            stage=("stage_for_ep", "first"),
            start_local=("watch_dt", "min"),
            end_local=("watch_dt", "max"),
            n_epochs=("id", "count"),
        )
        .sort_values("episode_id")
    )
    out["duration_min"] = out["n_epochs"] * epoch_sec / 60.0
    return out


def compute_transition_matrix(night_df: pd.DataFrame) -> pd.DataFrame:
    d = night_df.sort_values("watch_ts_sec").copy()
    d = d[d["stage_label"].isin(STAGE_ORDER)]
    d["prev_stage"] = d["stage_label"].shift(1)
    d = d.dropna(subset=["prev_stage"])
    c = pd.crosstab(d["prev_stage"], d["stage_label"])
    c = c.reindex(index=STAGE_ORDER, columns=STAGE_ORDER, fill_value=0)
    return c


def compute_night_metrics(night_df: pd.DataFrame, epoch_sec: float, summary: NightSummary) -> dict:
    d = night_df.sort_values("watch_ts_sec").copy()
    stage_counts = d["stage_label"].value_counts()
    stage_mins = {s: float(stage_counts.get(s, 0) * epoch_sec / 60.0) for s in STAGE_ORDER}
    total_stage_min = float(sum(stage_mins.values()))
    stage_pct = {s: (stage_mins[s] / total_stage_min * 100.0 if total_stage_min > 0 else 0.0) for s in STAGE_ORDER}

    d["prev_stage"] = d["stage_label"].shift(1)
    transitions = int((d["stage_label"] != d["prev_stage"]).sum() - 1)
    transitions = max(transitions, 0)
    awakenings = int(((d["stage_label"] == "awake") & (d["prev_stage"].isin(["light", "deep", "rem"]))).sum())

    sleep_mask = d["stage_label"].isin(["light", "deep", "rem"])
    if sleep_mask.any():
        sleep_onset = d.loc[sleep_mask, "watch_dt"].min()
    else:
        sleep_onset = pd.NaT

    metrics = {
        "night_id": summary.night_id,
        "session_id": summary.session_id,
        "start_local": summary.start_local.isoformat(sep=" "),
        "end_local": summary.end_local.isoformat(sep=" "),
        "duration_min": round(summary.duration_min, 2),
        "n_rows": int(summary.n_rows),
        "epoch_sec": round(summary.epoch_sec, 2),
        "sleep_onset_local": None if pd.isna(sleep_onset) else sleep_onset.isoformat(sep=" "),
        "sleep_total_min": round(stage_mins["light"] + stage_mins["deep"] + stage_mins["rem"], 2),
        "awake_min": round(stage_mins["awake"], 2),
        "light_min": round(stage_mins["light"], 2),
        "deep_min": round(stage_mins["deep"], 2),
        "rem_min": round(stage_mins["rem"], 2),
        "awake_pct": round(stage_pct["awake"], 2),
        "light_pct": round(stage_pct["light"], 2),
        "deep_pct": round(stage_pct["deep"], 2),
        "rem_pct": round(stage_pct["rem"], 2),
        "transitions": transitions,
        "awakenings": awakenings,
        "median_bpm": float(d["bpm"].median()),
        "median_sdhr": float(d["sdhr"].median()),
        "median_movement": float(d["movement"].median()),
        "lag_sec_mean": float(d["lag_sec"].mean()),
        "lag_sec_min": float(d["lag_sec"].min()),
        "lag_sec_max": float(d["lag_sec"].max()),
        "missing_bpm": int(d["bpm"].isna().sum()),
        "missing_sdhr": int(d["sdhr"].isna().sum()),
        "missing_movement": int(d["movement"].isna().sum()),
    }
    return metrics


def _style_time_axis(ax: plt.Axes) -> None:
    locator = mdates.AutoDateLocator(minticks=4, maxticks=10)
    formatter = mdates.DateFormatter("%H:%M")
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.grid(True, axis="x", alpha=0.25)


def _write_plotly_html_with_fallback(fig, outpath: Path, include_plotlyjs: str | bool) -> None:
    try:
        fig.write_html(str(outpath), include_plotlyjs=include_plotlyjs)
    except OSError as exc:
        # Embedded Plotly JS can be large; fallback to CDN mode on low-disk errors.
        if getattr(exc, "errno", None) == 28 and include_plotlyjs is True:
            fig.write_html(str(outpath), include_plotlyjs="cdn")
            return
        raise


def plot_night_overview(night_df: pd.DataFrame, episodes: pd.DataFrame, outpath: Path, dpi: int) -> None:
    d = night_df.sort_values("watch_dt").copy()
    fig, axes = plt.subplots(
        nrows=5,
        ncols=1,
        figsize=(16, 12),
        sharex=True,
        gridspec_kw={"height_ratios": [1.4, 1.2, 1.2, 1.2, 0.8]},
    )

    stage_y = {"deep": 0, "light": 1, "rem": 2, "awake": 3}
    y = d["stage_label"].map(stage_y)

    for _, ep in episodes.iterrows():
        c = STAGE_COLORS.get(ep["stage"], STAGE_COLORS["other"])
        axes[0].axvspan(ep["start_local"], ep["end_local"], color=c, alpha=0.16, lw=0)

    axes[0].step(d["watch_dt"], y, where="post", color="#111111", linewidth=1.4)
    axes[0].scatter(
        d["watch_dt"],
        y,
        c=d["stage_label"].map(lambda s: STAGE_COLORS.get(s, STAGE_COLORS["other"])),
        s=10,
        alpha=0.8,
    )
    axes[0].set_yticks([0, 1, 2, 3])
    axes[0].set_yticklabels(["Deep", "Light", "REM", "Awake"])
    axes[0].set_title("Sleep Stage Timeline (Hypnogram)")
    axes[0].set_ylabel("Stage")

    axes[1].plot(d["watch_dt"], d["movement"], color="#457b9d", linewidth=1.1)
    axes[1].set_ylabel("Movement")
    axes[1].set_title("Movement")

    axes[2].plot(d["watch_dt"], d["bpm"], color="#d62828", linewidth=1.1)
    axes[2].set_ylabel("BPM")
    axes[2].set_title("Heart Rate")

    axes[3].plot(d["watch_dt"], d["sdhr"], color="#f4a261", linewidth=1.1)
    axes[3].set_ylabel("sdHR")
    axes[3].set_title("Heart Rate Variability Proxy (sdHR)")

    for mode in sorted(d["source_mode"].dropna().unique()):
        mask = d["source_mode"] == mode
        axes[4].scatter(
            d.loc[mask, "watch_dt"],
            d.loc[mask, "source_mode"],
            s=10,
            color=SOURCE_MODE_COLORS.get(int(mode), "#999999"),
            label=SOURCE_MODE_LABEL.get(int(mode), str(mode)),
        )
    axes[4].set_ylim(-0.5, 1.5)
    axes[4].set_yticks([0, 1])
    axes[4].set_yticklabels(["movement", "hrm"])
    axes[4].set_ylabel("Mode")
    axes[4].set_title("Classifier Source Mode")
    axes[4].legend(loc="upper right", frameon=False)

    for ax in axes:
        _style_time_axis(ax)
    axes[-1].set_xlabel("Local Time")
    fig.tight_layout()
    fig.savefig(outpath, dpi=dpi)
    plt.close(fig)


def plot_stage_composition(night_df: pd.DataFrame, epoch_sec: float, outpath: Path, dpi: int) -> None:
    counts = night_df["stage_label"].value_counts()
    mins = np.array([counts.get(s, 0) * epoch_sec / 60.0 for s in STAGE_ORDER], dtype=float)
    total = mins.sum() if mins.sum() > 0 else 1.0
    pct = mins / total * 100.0

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(
        STAGE_ORDER,
        mins,
        color=[STAGE_COLORS[s] for s in STAGE_ORDER],
        edgecolor="#222222",
        linewidth=0.8,
    )
    for i, b in enumerate(bars):
        ax.text(
            b.get_x() + b.get_width() / 2,
            b.get_height() + max(mins) * 0.02 + 0.1,
            f"{mins[i]:.1f} min\n{pct[i]:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    ax.set_title("Stage Composition")
    ax.set_ylabel("Minutes")
    ax.grid(True, axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(outpath, dpi=dpi)
    plt.close(fig)


def plot_transition_matrix(night_df: pd.DataFrame, outpath: Path, dpi: int) -> None:
    c = compute_transition_matrix(night_df)
    fig, ax = plt.subplots(figsize=(7, 6))
    sns.heatmap(c, annot=True, fmt="d", cmap="YlGnBu", linewidths=0.5, cbar=False, ax=ax)
    ax.set_title("Stage Transition Matrix")
    ax.set_xlabel("To Stage")
    ax.set_ylabel("From Stage")
    fig.tight_layout()
    fig.savefig(outpath, dpi=dpi)
    plt.close(fig)


def plot_episode_durations(episodes: pd.DataFrame, outpath: Path, dpi: int) -> None:
    d = episodes[episodes["stage"].isin(STAGE_ORDER)].copy()
    fig, ax = plt.subplots(figsize=(10, 5))
    if d.empty:
        ax.text(0.5, 0.5, "No episodes available", ha="center", va="center", transform=ax.transAxes)
        ax.set_axis_off()
    else:
        sns.boxplot(
            data=d,
            x="stage",
            y="duration_min",
            hue="stage",
            order=STAGE_ORDER,
            hue_order=STAGE_ORDER,
            palette=STAGE_COLORS,
            dodge=False,
            ax=ax,
        )
        leg = ax.get_legend()
        if leg is not None:
            leg.remove()
        ax.set_title("Episode Duration by Stage")
        ax.set_xlabel("Stage")
        ax.set_ylabel("Episode Duration (min)")
        ax.grid(True, axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(outpath, dpi=dpi)
    plt.close(fig)


def plot_feature_space(night_df: pd.DataFrame, outpath: Path, dpi: int) -> None:
    d = night_df[night_df["stage_label"].isin(STAGE_ORDER)].copy()
    palette = {s: STAGE_COLORS[s] for s in STAGE_ORDER}

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.scatterplot(
        data=d,
        x="movement",
        y="bpm",
        hue="stage_label",
        hue_order=STAGE_ORDER,
        palette=palette,
        s=28,
        alpha=0.7,
        ax=axes[0],
    )
    axes[0].set_title("Movement vs BPM")
    axes[0].set_xlabel("Movement")
    axes[0].set_ylabel("BPM")
    axes[0].grid(True, alpha=0.2)

    sns.scatterplot(
        data=d,
        x="bpm",
        y="sdhr",
        hue="stage_label",
        hue_order=STAGE_ORDER,
        palette=palette,
        s=28,
        alpha=0.7,
        ax=axes[1],
        legend=False,
    )
    axes[1].set_title("BPM vs sdHR")
    axes[1].set_xlabel("BPM")
    axes[1].set_ylabel("sdHR")
    axes[1].grid(True, alpha=0.2)

    handles, labels = axes[0].get_legend_handles_labels()
    if handles and labels:
        axes[0].legend(handles=handles, labels=labels, title="Stage", frameon=False)
    fig.tight_layout()
    fig.savefig(outpath, dpi=dpi)
    plt.close(fig)


def plot_data_integrity(raw_night_df: pd.DataFrame, outpath: Path, dpi: int) -> None:
    d = raw_night_df.sort_values(["watch_ts_sec", "recv_ts_ms", "id"]).copy()
    d["dt_watch_sec"] = d["watch_ts_sec"].diff()
    d["dseq"] = d["sequence"].diff()

    fig, axes = plt.subplots(4, 1, figsize=(14, 11), sharex=False)

    axes[0].plot(d["watch_dt"], d["dt_watch_sec"], color="#5e548e", linewidth=1.0)
    axes[0].axhline(60, color="#999999", linestyle="--", linewidth=0.9)
    axes[0].set_ylabel("sec")
    axes[0].set_title("Inter-epoch interval (watch_ts delta)")
    axes[0].grid(True, alpha=0.25)

    axes[1].plot(d["watch_dt"], d["dseq"], color="#9c6644", linewidth=1.0)
    axes[1].axhline(1, color="#999999", linestyle="--", linewidth=0.9)
    axes[1].set_ylabel("delta")
    axes[1].set_title("Sequence delta")
    axes[1].grid(True, alpha=0.25)

    axes[2].plot(d["watch_dt"], d["lag_sec"], color="#3a86ff", linewidth=1.0)
    axes[2].axhline(0, color="#999999", linestyle="--", linewidth=0.9)
    axes[2].set_ylabel("sec")
    axes[2].set_title("Receiver lag (recv - watch)")
    axes[2].grid(True, alpha=0.25)

    miss = pd.Series(
        {
            "movement": d["movement"].isna().mean() * 100.0,
            "bpm": d["bpm"].isna().mean() * 100.0,
            "sdhr": d["sdhr"].isna().mean() * 100.0,
        }
    )
    axes[3].bar(miss.index, miss.values, color=["#457b9d", "#d62828", "#f4a261"])
    axes[3].set_ylim(0, max(5.0, miss.max() * 1.25 + 1.0))
    axes[3].set_ylabel("missing %")
    axes[3].set_title("Signal missingness")
    axes[3].grid(True, axis="y", alpha=0.25)

    for ax in axes[:3]:
        _style_time_axis(ax)
    axes[2].set_xlabel("Local Time")
    fig.tight_layout()
    fig.savefig(outpath, dpi=dpi)
    plt.close(fig)


def save_interactive_html(
    night_df: pd.DataFrame,
    outpath: Path,
    include_plotlyjs: str | bool = "cdn",
) -> None:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    d = night_df.sort_values("watch_dt").copy()
    stage_y = {"deep": 0, "light": 1, "rem": 2, "awake": 3}

    fig = make_subplots(
        rows=5,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_heights=[0.2, 0.22, 0.22, 0.22, 0.14],
        subplot_titles=("Stage", "Movement", "BPM", "sdHR", "Source Mode"),
    )

    fig.add_trace(
        go.Scatter(
            x=d["watch_dt"],
            y=d["stage_label"].map(stage_y),
            mode="lines+markers",
            name="stage",
            marker=dict(size=5),
            line=dict(width=1.2, color="#111111"),
        ),
        row=1,
        col=1,
    )
    fig.add_trace(go.Scatter(x=d["watch_dt"], y=d["movement"], mode="lines", name="movement"), row=2, col=1)
    fig.add_trace(go.Scatter(x=d["watch_dt"], y=d["bpm"], mode="lines", name="bpm"), row=3, col=1)
    fig.add_trace(go.Scatter(x=d["watch_dt"], y=d["sdhr"], mode="lines", name="sdhr"), row=4, col=1)
    fig.add_trace(
        go.Scatter(x=d["watch_dt"], y=d["source_mode"], mode="markers", name="source_mode", marker=dict(size=5)),
        row=5,
        col=1,
    )

    fig.update_yaxes(title_text="Stage", tickvals=[0, 1, 2, 3], ticktext=["Deep", "Light", "REM", "Awake"], row=1, col=1)
    fig.update_yaxes(title_text="Mode", tickvals=[0, 1], ticktext=["movement", "hrm"], row=5, col=1)
    fig.update_layout(
        height=980,
        width=1400,
        title_text="Sleep Night Interactive Timeline",
        legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="left", x=0),
    )
    _write_plotly_html_with_fallback(fig, outpath, include_plotlyjs)


def _kappa_from_confusion(cm: pd.DataFrame) -> float:
    n = float(cm.values.sum())
    if n <= 0:
        return float("nan")
    po = float(np.trace(cm.values) / n)
    row_marg = cm.sum(axis=1).to_numpy(dtype=float)
    col_marg = cm.sum(axis=0).to_numpy(dtype=float)
    pe = float((row_marg * col_marg).sum() / (n * n))
    if abs(1.0 - pe) < 1e-12:
        return float("nan")
    return (po - pe) / (1.0 - pe)


def _prepare_ours_minute_table(night_df: pd.DataFrame) -> pd.DataFrame:
    ours = night_df[["watch_dt", "stage_label", "bpm", "movement", "sdhr"]].copy()
    ours["timestamp_local"] = ours["watch_dt"].dt.floor("min")
    ours = ours.drop_duplicates(subset=["timestamp_local"], keep="last")
    ours = ours.rename(columns={"stage_label": "ours_stage", "bpm": "ours_bpm"})
    ours["ours_stage_collapsed"] = ours["ours_stage"].map(_collapse_stage)
    return ours[["timestamp_local", "ours_stage", "ours_stage_collapsed", "ours_bpm", "movement", "sdhr"]]


def _prepare_withings_stage_table(withings_df: pd.DataFrame) -> pd.DataFrame:
    w = withings_df.copy()
    w["timestamp_local"] = pd.to_datetime(w["timestamp_local"]).dt.floor("min")
    w = w.drop_duplicates(subset=["timestamp_local"], keep="last")
    w = w.rename(columns={"stage_label": "withings_stage"})
    w["withings_stage_collapsed"] = w["withings_stage"].map(_collapse_stage)
    return w[["timestamp_local", "withings_stage", "withings_stage_collapsed"]]


def _prepare_withings_hr_table(withings_hr_df: pd.DataFrame) -> pd.DataFrame:
    w = withings_hr_df.copy()
    w["timestamp_local"] = pd.to_datetime(w["timestamp_local"]).dt.floor("min")
    w = w.groupby("timestamp_local", as_index=False)["hr_bpm"].median()
    return w


def build_aligned_compare_df(
    night_df: pd.DataFrame,
    withings_df: pd.DataFrame,
    withings_hr_df: Optional[pd.DataFrame] = None,
    window_mode: str = "overlap",
) -> Optional[dict]:
    ours = _prepare_ours_minute_table(night_df)
    w_stage = _prepare_withings_stage_table(withings_df)
    if ours.empty or w_stage.empty:
        return None

    # Guardrail: restrict Withings data to a neighborhood around this night.
    # Without this, passing a whole export directory can create a months-long
    # timeline and enormous HTML files.
    ours_min_raw = ours["timestamp_local"].min()
    ours_max_raw = ours["timestamp_local"].max()
    guard_start = ours_min_raw - pd.Timedelta(hours=18)
    guard_end = ours_max_raw + pd.Timedelta(hours=18)
    w_stage = w_stage[
        (w_stage["timestamp_local"] >= guard_start)
        & (w_stage["timestamp_local"] <= guard_end)
    ].copy()
    if w_stage.empty:
        return None

    ours_min, ours_max = ours["timestamp_local"].min(), ours["timestamp_local"].max()
    with_min, with_max = w_stage["timestamp_local"].min(), w_stage["timestamp_local"].max()
    overlap_start = max(ours_min, with_min)
    overlap_end = min(ours_max, with_max)
    if overlap_end < overlap_start:
        return None

    full_start = min(ours_min, with_min)
    full_end = max(ours_max, with_max)
    if window_mode == "overlap":
        start, end = overlap_start, overlap_end
    else:
        start, end = full_start, full_end

    idx = pd.date_range(start=start, end=end, freq="1min")
    aligned = pd.DataFrame({"timestamp_local": idx})
    aligned = aligned.merge(ours, on="timestamp_local", how="left")
    aligned = aligned.merge(w_stage, on="timestamp_local", how="left")

    if withings_hr_df is not None:
        w_hr = _prepare_withings_hr_table(withings_hr_df)
        w_hr = w_hr[
            (w_hr["timestamp_local"] >= guard_start)
            & (w_hr["timestamp_local"] <= guard_end)
        ].copy()
        aligned = aligned.merge(w_hr, on="timestamp_local", how="left")
    else:
        aligned["hr_bpm"] = np.nan

    for c in ["ours_stage", "ours_stage_collapsed", "withings_stage", "withings_stage_collapsed"]:
        aligned[c] = aligned[c].ffill(limit=2)

    strict_valid = aligned["ours_stage"].notna() & aligned["withings_stage"].notna()
    coll_valid = aligned["ours_stage_collapsed"].notna() & aligned["withings_stage_collapsed"].notna()
    aligned["stage_match_strict"] = strict_valid & (aligned["ours_stage"] == aligned["withings_stage"])
    aligned["stage_match_collapsed"] = coll_valid & (
        aligned["ours_stage_collapsed"] == aligned["withings_stage_collapsed"]
    )
    aligned["bpm_delta"] = aligned["ours_bpm"] - aligned["hr_bpm"]

    return {
        "aligned": aligned,
        "full_start": full_start,
        "full_end": full_end,
        "overlap_start": overlap_start,
        "overlap_end": overlap_end,
    }


def _compute_stage_metrics(aligned: pd.DataFrame, mode: str) -> Optional[dict]:
    if mode == "collapsed":
        truth_col = "withings_stage_collapsed"
        pred_col = "ours_stage_collapsed"
        order = STAGE_ORDER_COLLAPSED
    else:
        truth_col = "withings_stage"
        pred_col = "ours_stage"
        order = STAGE_ORDER

    valid = aligned[truth_col].isin(order) & aligned[pred_col].isin(order)
    d = aligned.loc[valid, ["timestamp_local", truth_col, pred_col]].copy()
    if len(d) < 15:
        return None

    cm = pd.crosstab(d[truth_col], d[pred_col]).reindex(index=order, columns=order, fill_value=0)
    acc = float((d[truth_col] == d[pred_col]).mean())
    kappa = _kappa_from_confusion(cm)

    per_stage_rows = []
    for s in order:
        tp = float(cm.loc[s, s])
        true_sum = float(cm.loc[s].sum())
        pred_sum = float(cm[s].sum())
        recall = tp / true_sum if true_sum > 0 else np.nan
        precision = tp / pred_sum if pred_sum > 0 else np.nan
        per_stage_rows.append(
            {
                "stage": s,
                "precision": precision,
                "recall": recall,
                "support_true": true_sum,
                "support_pred": pred_sum,
            }
        )

    return {
        "n_overlap_minutes": int(len(d)),
        "accuracy": acc,
        "cohen_kappa": kappa,
        "cm": cm,
        "per_stage": pd.DataFrame(per_stage_rows),
        "aligned": d,
    }


def save_interactive_compare_html(
    night_df: pd.DataFrame,
    withings_df: pd.DataFrame,
    withings_hr_df: Optional[pd.DataFrame],
    outpath: Path,
    window_mode: str,
    include_plotlyjs: str | bool = "cdn",
) -> Optional[dict]:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    built = build_aligned_compare_df(
        night_df,
        withings_df,
        withings_hr_df=withings_hr_df,
        window_mode="full",
    )
    if built is None:
        return None

    d = built["aligned"].copy()
    strict_map = {"deep": 0, "light": 1, "rem": 2, "awake": 3}
    coll_map = {"deep": 0, "light": 1, "awake": 2}
    d["ours_strict_y"] = d["ours_stage"].map(strict_map)
    d["withings_strict_y"] = d["withings_stage"].map(strict_map)
    d["ours_coll_y"] = d["ours_stage_collapsed"].map(coll_map)
    d["withings_coll_y"] = d["withings_stage_collapsed"].map(coll_map)
    d["mismatch_strict"] = (~d["stage_match_strict"]).astype(float)
    d["mismatch_collapsed"] = (~d["stage_match_collapsed"]).astype(float)

    fig = make_subplots(
        rows=6,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.025,
        row_heights=[0.2, 0.1, 0.18, 0.14, 0.18, 0.2],
        subplot_titles=(
            "Stage Overlay",
            "Stage Mismatch (1 = disagreement)",
            "Heart Rate Overlay",
            "Heart Rate Delta (SleepStream - Withings)",
            "Movement",
            "sdHR",
        ),
    )

    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["ours_strict_y"], mode="lines", name="ours stage (strict)", line=dict(color="#e76f51", width=1.8)), row=1, col=1)
    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["withings_strict_y"], mode="lines", name="withings stage (strict)", line=dict(color="#264653", width=1.8)), row=1, col=1)
    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["ours_coll_y"], mode="lines", name="ours stage (collapsed)", line=dict(color="#e76f51", width=1.8), visible=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["withings_coll_y"], mode="lines", name="withings stage (collapsed)", line=dict(color="#264653", width=1.8), visible=False), row=1, col=1)

    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["mismatch_strict"], mode="lines", fill="tozeroy", name="mismatch strict", line=dict(color="#d62828", width=1.2)), row=2, col=1)
    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["mismatch_collapsed"], mode="lines", fill="tozeroy", name="mismatch collapsed", line=dict(color="#f4a261", width=1.2), visible=False), row=2, col=1)

    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["ours_bpm"], mode="lines", name="ours bpm", line=dict(color="#d62828", width=1.4)), row=3, col=1)
    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["hr_bpm"], mode="lines", name="withings bpm", line=dict(color="#264653", width=1.3)), row=3, col=1)
    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["bpm_delta"], mode="lines", name="bpm delta", line=dict(color="#1d3557", width=1.1)), row=4, col=1)
    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["movement"], mode="lines", name="movement", line=dict(color="#457b9d", width=1.1)), row=5, col=1)
    fig.add_trace(go.Scatter(x=d["timestamp_local"], y=d["sdhr"], mode="lines", name="sdhr", line=dict(color="#f4a261", width=1.1)), row=6, col=1)

    fig.update_yaxes(title_text="Stage", tickvals=[0, 1, 2, 3], ticktext=["Deep", "Light", "REM", "Awake"], row=1, col=1)
    fig.update_yaxes(title_text="Mismatch", range=[0, 1.05], row=2, col=1)
    fig.update_yaxes(title_text="BPM", row=3, col=1)
    fig.update_yaxes(title_text="Delta", row=4, col=1)
    fig.update_yaxes(title_text="Move", row=5, col=1)
    fig.update_yaxes(title_text="sdHR", row=6, col=1)
    fig.update_xaxes(title_text="Local Time", row=6, col=1)

    full_range = [built["full_start"], built["full_end"]]
    overlap_range = [built["overlap_start"], built["overlap_end"]]
    default_range = overlap_range if window_mode == "overlap" else full_range

    n_traces = len(fig.data)
    vis_strict = [False] * n_traces
    vis_coll = [False] * n_traces
    for i in [0, 1, 4, 6, 7, 8, 9, 10]:
        vis_strict[i] = True
    for i in [2, 3, 5, 6, 7, 8, 9, 10]:
        vis_coll[i] = True

    range_relayout_full = {f"xaxis{i if i > 1 else ''}.range": full_range for i in range(1, 7)}
    range_relayout_overlap = {f"xaxis{i if i > 1 else ''}.range": overlap_range for i in range(1, 7)}

    fig.update_layout(
        title="Interactive SleepStream vs Withings Compare",
        height=1200,
        width=1500,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                x=0.01,
                y=1.14,
                showactive=True,
                buttons=[
                    dict(label="Strict stage mode", method="update", args=[{"visible": vis_strict}]),
                    dict(label="Collapsed stage mode", method="update", args=[{"visible": vis_coll}]),
                ],
            ),
            dict(
                type="buttons",
                direction="right",
                x=0.40,
                y=1.14,
                showactive=True,
                buttons=[
                    dict(label="Full window", method="relayout", args=[range_relayout_full]),
                    dict(label="Overlap window", method="relayout", args=[range_relayout_overlap]),
                ],
            ),
        ],
    )
    fig.update_xaxes(range=default_range)
    _write_plotly_html_with_fallback(fig, outpath, include_plotlyjs)
    return built


def compare_with_withings(
    night_df: pd.DataFrame,
    withings_df: pd.DataFrame,
    outdir: Path,
    night_id: str,
    dpi: int,
    stage_compare_mode: str = "both",
    window_mode: str = "overlap",
) -> Optional[dict]:
    built = build_aligned_compare_df(night_df, withings_df, withings_hr_df=None, window_mode=window_mode)
    if built is None:
        return None
    aligned = built["aligned"]
    aligned.to_csv(outdir / "withings_stage_aligned.csv", index=False)

    strict = _compute_stage_metrics(aligned, mode="strict")
    collapsed = _compute_stage_metrics(aligned, mode="collapsed")
    if strict is None and collapsed is None:
        return None

    if strict is not None:
        cm = strict["cm"]
        fig, ax = plt.subplots(figsize=(7, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="OrRd", linewidths=0.5, cbar=False, ax=ax)
        ax.set_title("Withings vs SleepStream Confusion Matrix (Strict)")
        ax.set_xlabel("Predicted (SleepStream)")
        ax.set_ylabel("Reference (Withings)")
        fig.tight_layout()
        fig.savefig(outdir / "withings_confusion.png", dpi=dpi)
        plt.close(fig)
        strict["per_stage"].to_csv(outdir / "withings_per_stage_metrics.csv", index=False)

        s = strict["aligned"]
        stage_y = {"deep": 0, "light": 1, "rem": 2, "awake": 3}
        fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True, gridspec_kw={"height_ratios": [1, 1]})
        axes[0].step(s["timestamp_local"], s["withings_stage"].map(stage_y), where="post", color="#264653", linewidth=1.2)
        axes[0].set_yticks([0, 1, 2, 3])
        axes[0].set_yticklabels(["Deep", "Light", "REM", "Awake"])
        axes[0].set_title("Withings Stages")
        axes[1].step(s["timestamp_local"], s["ours_stage"].map(stage_y), where="post", color="#e76f51", linewidth=1.2)
        axes[1].set_yticks([0, 1, 2, 3])
        axes[1].set_yticklabels(["Deep", "Light", "REM", "Awake"])
        axes[1].set_title("SleepStream Stages")
        for ax in axes:
            _style_time_axis(ax)
        axes[-1].set_xlabel("Local Time")
        fig.suptitle(f"Withings Comparison - {night_id}")
        fig.tight_layout()
        fig.savefig(outdir / "withings_overlay.png", dpi=dpi)
        plt.close(fig)

    if collapsed is not None:
        cmc = collapsed["cm"]
        fig, ax = plt.subplots(figsize=(7, 6))
        sns.heatmap(cmc, annot=True, fmt="d", cmap="YlGnBu", linewidths=0.5, cbar=False, ax=ax)
        ax.set_title("Withings vs SleepStream Confusion Matrix (Collapsed)")
        ax.set_xlabel("Predicted (SleepStream)")
        ax.set_ylabel("Reference (Withings)")
        fig.tight_layout()
        fig.savefig(outdir / "withings_confusion_collapsed.png", dpi=dpi)
        plt.close(fig)
        collapsed["per_stage"].to_csv(outdir / "withings_per_stage_metrics_collapsed.csv", index=False)

    strict_json = None
    collapsed_json = None
    if strict is not None:
        strict_json = {
            "night_id": night_id,
            "mode": "strict",
            "n_overlap_minutes": strict["n_overlap_minutes"],
            "accuracy": strict["accuracy"],
            "cohen_kappa": strict["cohen_kappa"],
        }
        with open(outdir / "withings_metrics_strict.json", "w", encoding="utf-8") as f:
            json.dump(strict_json, f, indent=2)

    if collapsed is not None:
        collapsed_json = {
            "night_id": night_id,
            "mode": "collapsed",
            "n_overlap_minutes": collapsed["n_overlap_minutes"],
            "accuracy": collapsed["accuracy"],
            "cohen_kappa": collapsed["cohen_kappa"],
        }
        with open(outdir / "withings_metrics_collapsed.json", "w", encoding="utf-8") as f:
            json.dump(collapsed_json, f, indent=2)

    if stage_compare_mode == "strict":
        selected = strict_json or collapsed_json
    elif stage_compare_mode == "collapsed":
        selected = collapsed_json or strict_json
    else:
        selected = strict_json or collapsed_json

    if selected is None:
        return None

    with open(outdir / "withings_metrics.json", "w", encoding="utf-8") as f:
        json.dump(selected, f, indent=2)
    return selected


def compare_with_withings_hr(
    night_df: pd.DataFrame,
    withings_hr_df: pd.DataFrame,
    outdir: Path,
    night_id: str,
    dpi: int,
    window_mode: str = "overlap",
) -> Optional[dict]:
    ours = night_df[["watch_dt", "bpm"]].copy().dropna(subset=["bpm"])
    ours["timestamp_local"] = ours["watch_dt"].dt.floor("min")
    ours = ours.groupby("timestamp_local", as_index=False)["bpm"].median()
    ours = ours.rename(columns={"bpm": "ours_bpm"})

    w = _prepare_withings_hr_table(withings_hr_df)
    if w.empty:
        return None

    full_start = min(ours["timestamp_local"].min(), w["timestamp_local"].min())
    full_end = max(ours["timestamp_local"].max(), w["timestamp_local"].max())
    overlap_start = max(ours["timestamp_local"].min(), w["timestamp_local"].min())
    overlap_end = min(ours["timestamp_local"].max(), w["timestamp_local"].max())
    if overlap_end < overlap_start:
        return None

    if window_mode == "overlap":
        window_start, window_end = overlap_start, overlap_end
    else:
        window_start, window_end = full_start, full_end

    ours = ours[(ours["timestamp_local"] >= window_start) & (ours["timestamp_local"] <= window_end)]
    w = w[(w["timestamp_local"] >= window_start) & (w["timestamp_local"] <= window_end)]
    merged = pd.merge(ours, w, on="timestamp_local", how="inner")
    if len(merged) < 15:
        return None

    diff = merged["ours_bpm"] - merged["hr_bpm"]
    mae = float(np.abs(diff).mean())
    bias = float(diff.mean())
    rmse = float(np.sqrt((diff * diff).mean()))
    corr = float(merged[["ours_bpm", "hr_bpm"]].corr().iloc[0, 1])

    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)
    axes[0].plot(merged["timestamp_local"], merged["ours_bpm"], label="SleepStream bpm", color="#d62828")
    axes[0].plot(merged["timestamp_local"], merged["hr_bpm"], label="Withings bpm", color="#264653", alpha=0.8)
    axes[0].set_ylabel("BPM")
    axes[0].set_title("Heart Rate Comparison")
    axes[0].legend(frameon=False)
    axes[0].grid(True, alpha=0.25)

    axes[1].plot(merged["timestamp_local"], diff, color="#1d3557")
    axes[1].axhline(0, color="#999999", linestyle="--", linewidth=0.9)
    axes[1].set_ylabel("Delta BPM")
    axes[1].set_title("SleepStream - Withings")
    axes[1].grid(True, alpha=0.25)
    _style_time_axis(axes[0])
    _style_time_axis(axes[1])
    axes[1].set_xlabel("Local Time")
    fig.suptitle(f"Withings HR Comparison - {night_id}")
    fig.tight_layout()
    fig.savefig(outdir / "withings_hr_overlay.png", dpi=dpi)
    plt.close(fig)

    metrics = {
        "night_id": night_id,
        "n_overlap_points": int(len(merged)),
        "hr_mae": mae,
        "hr_rmse": rmse,
        "hr_bias": bias,
        "hr_corr": corr,
    }
    with open(outdir / "withings_hr_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    merged.to_csv(outdir / "withings_hr_aligned.csv", index=False)
    return metrics


def compare_with_withings_sleep_summary(
    summary: NightSummary,
    withings_summary_df: pd.DataFrame,
    outdir: Path,
) -> Optional[dict]:
    ours_start = pd.Timestamp(summary.start_local)
    ours_end = pd.Timestamp(summary.end_local)
    ours_mid = ours_start + (ours_end - ours_start) / 2

    ws = withings_summary_df.copy()
    ws["mid"] = ws["from_local"] + (ws["to_local"] - ws["from_local"]) / 2
    ws["mid_dist_sec"] = (ws["mid"] - ours_mid).abs().dt.total_seconds()
    ws = ws.sort_values("mid_dist_sec")
    if ws.empty:
        return None

    best = ws.iloc[0]
    if float(best["mid_dist_sec"]) > 12 * 3600:
        return None

    out = {
        "withings_from_local": pd.Timestamp(best["from_local"]).isoformat(sep=" "),
        "withings_to_local": pd.Timestamp(best["to_local"]).isoformat(sep=" "),
        "withings_duration_min": float(best.get("duration_min", np.nan)),
        "withings_light_min": float(best.get("light_min", np.nan)),
        "withings_deep_min": float(best.get("deep_min", np.nan)),
        "withings_rem_min": float(best.get("rem_min", np.nan)),
        "withings_awake_min": float(best.get("awake_min", np.nan)),
        "withings_avg_hr": float(best.get("avg_hr", np.nan)),
        "withings_min_hr": float(best.get("min_hr", np.nan)),
        "withings_max_hr": float(best.get("max_hr", np.nan)),
    }
    with open(outdir / "withings_sleep_summary_match.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    return out


def plot_cross_night_trends(summary_df: pd.DataFrame, outpath: Path, dpi: int) -> None:
    if summary_df.empty:
        return

    d = summary_df.copy().sort_values("start_local")
    d["start_local_dt"] = pd.to_datetime(d["start_local"])
    d["end_local_dt"] = pd.to_datetime(d["end_local"])
    d["night_label"] = d["night_id"]

    fig, axes = plt.subplots(3, 1, figsize=(15, 11), sharex=True)

    axes[0].plot(d["night_label"], d["duration_min"], marker="o", color="#1d3557", label="session duration")
    axes[0].plot(d["night_label"], d["sleep_total_min"], marker="o", color="#2a9d8f", label="sleep total")
    axes[0].set_ylabel("minutes")
    axes[0].set_title("Night Duration and Total Sleep Proxy")
    axes[0].legend(frameon=False)
    axes[0].grid(True, alpha=0.25)

    bottom = np.zeros(len(d), dtype=float)
    for key in ["awake_pct", "light_pct", "deep_pct", "rem_pct"]:
        stage = key.replace("_pct", "")
        vals = d[key].to_numpy(dtype=float)
        axes[1].bar(d["night_label"], vals, bottom=bottom, color=STAGE_COLORS[stage], label=stage)
        bottom += vals
    axes[1].set_ylabel("percent")
    axes[1].set_ylim(0, 100)
    axes[1].set_title("Stage Composition by Night")
    axes[1].legend(frameon=False, ncol=4)

    onset_hour = pd.to_datetime(d["sleep_onset_local"], errors="coerce").dt.hour + (
        pd.to_datetime(d["sleep_onset_local"], errors="coerce").dt.minute / 60.0
    )
    wake_hour = d["end_local_dt"].dt.hour + d["end_local_dt"].dt.minute / 60.0
    axes[2].plot(d["night_label"], onset_hour, marker="o", color="#e76f51", label="sleep onset")
    axes[2].plot(d["night_label"], wake_hour, marker="o", color="#264653", label="wake time")
    axes[2].set_ylabel("clock hour")
    axes[2].set_ylim(0, 24)
    axes[2].set_title("Onset and Wake Time")
    axes[2].legend(frameon=False)
    axes[2].grid(True, alpha=0.25)
    axes[2].set_xlabel("Night")

    for label in axes[2].get_xticklabels():
        label.set_rotation(20)
        label.set_horizontalalignment("right")

    fig.tight_layout()
    fig.savefig(outpath, dpi=dpi)
    plt.close(fig)


def generate_for_night(
    raw_session_df: pd.DataFrame,
    ana_session_df: pd.DataFrame,
    summary: NightSummary,
    outdir: Path,
    dpi: int,
    withings_df: Optional[pd.DataFrame] = None,
    withings_hr_df: Optional[pd.DataFrame] = None,
    withings_nights_df: Optional[pd.DataFrame] = None,
    stage_compare_mode: str = "both",
    compare_window: str = "overlap",
    compare_interactive: bool = True,
    include_plotlyjs: str | bool = True,
) -> dict:
    outdir.mkdir(parents=True, exist_ok=True)
    episodes = get_episodes(ana_session_df, summary.epoch_sec)
    metrics = compute_night_metrics(ana_session_df, summary.epoch_sec, summary)

    plot_night_overview(ana_session_df, episodes, outdir / "night_overview.png", dpi=dpi)
    plot_stage_composition(ana_session_df, summary.epoch_sec, outdir / "stage_composition.png", dpi=dpi)
    plot_transition_matrix(ana_session_df, outdir / "transition_matrix.png", dpi=dpi)
    plot_episode_durations(episodes, outdir / "episode_durations.png", dpi=dpi)
    plot_feature_space(ana_session_df, outdir / "feature_space.png", dpi=dpi)
    plot_data_integrity(raw_session_df, outdir / "data_integrity.png", dpi=dpi)
    save_interactive_html(
        ana_session_df,
        outdir / "interactive_timeline.html",
        include_plotlyjs=include_plotlyjs,
    )

    if withings_df is not None:
        comparison = compare_with_withings(
            ana_session_df,
            withings_df,
            outdir=outdir,
            night_id=summary.night_id,
            dpi=dpi,
            stage_compare_mode=stage_compare_mode,
            window_mode=compare_window,
        )
        if comparison is not None:
            metrics.update(
                {
                    "withings_overlap_min": comparison["n_overlap_minutes"],
                    "withings_accuracy": comparison["accuracy"],
                    "withings_kappa": comparison["cohen_kappa"],
                    "withings_compare_mode": comparison.get("mode", "strict"),
                }
            )

        if compare_interactive:
            save_interactive_compare_html(
                ana_session_df,
                withings_df,
                withings_hr_df=withings_hr_df,
                outpath=outdir / "interactive_compare_timeline.html",
                window_mode=compare_window,
                include_plotlyjs=include_plotlyjs,
            )

    if withings_hr_df is not None:
        hr_comparison = compare_with_withings_hr(
            ana_session_df,
            withings_hr_df,
            outdir=outdir,
            night_id=summary.night_id,
            dpi=dpi,
            window_mode=compare_window,
        )
        if hr_comparison is not None:
            metrics.update(
                {
                    "withings_hr_points": hr_comparison["n_overlap_points"],
                    "withings_hr_mae": hr_comparison["hr_mae"],
                    "withings_hr_rmse": hr_comparison["hr_rmse"],
                    "withings_hr_bias": hr_comparison["hr_bias"],
                    "withings_hr_corr": hr_comparison["hr_corr"],
                }
            )

    if withings_nights_df is not None:
        night_match = compare_with_withings_sleep_summary(summary, withings_nights_df, outdir=outdir)
        if night_match is not None:
            metrics.update(night_match)

    with open(outdir / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    pd.DataFrame([metrics]).to_csv(outdir / "metrics.csv", index=False)
    episodes.to_csv(outdir / "episodes.csv", index=False)
    return metrics


def select_sessions(
    sessions: pd.DataFrame,
    all_nights: bool,
    night_id: Optional[str],
    min_session_min: int,
) -> pd.DataFrame:
    s = sessions[sessions["duration_min"] >= float(min_session_min)].copy()
    if s.empty:
        return s

    if night_id:
        return s[s["night_id"] == night_id].copy()
    if all_nights:
        return s
    idx = s["duration_min"].idxmax()
    return s.loc[[idx]].copy()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate SleepStream visualizations from sleepstream.db")
    p.add_argument("--db", default=None, help="SQLite database path (default: auto-detect sleepstream.db)")
    p.add_argument("--outdir", default=None, help="Output directory (default: receiver/plots)")
    p.add_argument("--all-nights", action="store_true", help="Generate outputs for all sessions above min duration")
    p.add_argument("--night-id", default=None, help="Generate outputs for one inferred night id")
    p.add_argument("--session-gap-min", type=int, default=120, help="Gap threshold in minutes for splitting sessions")
    p.add_argument("--min-session-min", type=int, default=30, help="Ignore sessions shorter than this")
    p.add_argument("--tz", choices=["local", "utc"], default="local", help="Timezone alignment for plots and metrics")
    p.add_argument(
        "--withings",
        default=None,
        help=(
            "Optional Withings export path. Can be a CSV file or an export "
            "directory containing raw_tracker_sleep-state.csv or sleep.csv"
        ),
    )
    p.add_argument(
        "--compare-window",
        choices=["overlap", "full"],
        default="overlap",
        help="Comparison window for Withings overlays/metrics",
    )
    p.add_argument(
        "--stage-compare-mode",
        choices=["strict", "collapsed", "both"],
        default="both",
        help="How to compare stages when Withings lacks REM",
    )
    p.add_argument(
        "--compare-interactive",
        action="store_true",
        help="Generate interactive compare timeline when Withings is provided",
    )
    p.add_argument(
        "--self-contained-html",
        action="store_true",
        help="Embed Plotly JS in HTML files for offline viewing",
    )
    p.add_argument("--dpi", type=int, default=150, help="PNG output DPI")
    return p


def main() -> None:
    args = build_parser().parse_args()
    db_path = resolve_db_path(args.db)
    if not db_path.exists():
        raise FileNotFoundError(f"Database not found: {db_path}")

    default_out = Path(__file__).resolve().parent / "plots"
    outdir = Path(args.outdir).expanduser().resolve() if args.outdir else default_out
    outdir.mkdir(parents=True, exist_ok=True)

    raw = load_sleep_updates(db_path, tz_mode=args.tz)
    raw, sessions = assign_sessions(raw, session_gap_min=args.session_gap_min)
    ana = dedupe_for_analysis(raw)

    selected = select_sessions(
        sessions,
        all_nights=args.all_nights,
        night_id=args.night_id,
        min_session_min=args.min_session_min,
    )
    if selected.empty:
        raise ValueError(
            "No sessions selected. Try lowering --min-session-min or use --all-nights to inspect all sessions."
        )

    withings_df = None
    withings_hr_df = None
    withings_nights_df = None
    if args.withings:
        withings_path = Path(args.withings).expanduser().resolve()
        if withings_path.is_dir():
            candidates = [
                withings_path / "raw_tracker_sleep-state.csv",
                withings_path / "sleep.csv",
            ]
            found = next((p for p in candidates if p.exists()), None)
            if found is None:
                raise FileNotFoundError(
                    "No supported Withings sleep CSV found in directory. "
                    "Expected one of: raw_tracker_sleep-state.csv, sleep.csv"
                )
            withings_df = load_withings_sleep(found, tz_mode=args.tz)

            hr_path = withings_path / "raw_hr_hr.csv"
            if hr_path.exists():
                try:
                    withings_hr_df = load_withings_hr(hr_path, tz_mode=args.tz)
                except Exception as exc:
                    print(f"Warning: failed to load Withings HR file: {hr_path} ({exc})")

            sleep_summary_path = withings_path / "sleep.csv"
            if sleep_summary_path.exists():
                try:
                    withings_nights_df = load_withings_nights_summary(sleep_summary_path, tz_mode=args.tz)
                except Exception as exc:
                    print(f"Warning: failed to load Withings sleep summary: {sleep_summary_path} ({exc})")
        else:
            withings_df = load_withings_sleep(withings_path, tz_mode=args.tz)

    all_metrics = []
    include_plotlyjs = True if args.self_contained_html else "cdn"
    for _, srow in selected.iterrows():
        sid = int(srow["session_id"])
        night_id = srow["night_id"]

        raw_session_df = raw[raw["session_id"] == sid].copy()
        ana_session_df = ana[ana["session_id"] == sid].copy()
        epoch_sec = infer_epoch_seconds(ana_session_df["watch_ts_sec"])

        summary = NightSummary(
            night_id=night_id,
            session_id=sid,
            start_local=pd.to_datetime(srow["start_local"]).to_pydatetime(),
            end_local=pd.to_datetime(srow["end_local"]).to_pydatetime(),
            duration_min=float(srow["duration_min"]),
            n_rows=int(len(ana_session_df)),
            epoch_sec=epoch_sec,
        )

        night_out = outdir / night_id
        metrics = generate_for_night(
            raw_session_df=raw_session_df,
            ana_session_df=ana_session_df,
            summary=summary,
            outdir=night_out,
            dpi=args.dpi,
            withings_df=withings_df,
            withings_hr_df=withings_hr_df,
            withings_nights_df=withings_nights_df,
            stage_compare_mode=args.stage_compare_mode,
            compare_window=args.compare_window,
            compare_interactive=args.compare_interactive,
            include_plotlyjs=include_plotlyjs,
        )
        all_metrics.append(metrics)

    summary_df = pd.DataFrame(all_metrics).sort_values("start_local")
    summary_df.to_csv(outdir / "all_nights_summary.csv", index=False)
    with open(outdir / "all_nights_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_df.to_dict(orient="records"), f, indent=2)
    plot_cross_night_trends(summary_df, outdir / "all_nights_trends.png", dpi=args.dpi)

    sessions.to_csv(outdir / "all_sessions_detected.csv", index=False)

    print(f"Database: {db_path}")
    print(f"Output:   {outdir}")
    print(f"Sessions: {len(selected)} generated, {len(sessions)} detected")
    print("Done.")


if __name__ == "__main__":
    sns.set_theme(style="whitegrid")
    main()
