"""Flexible parser for Withings sleep exports.

The exporter format can vary by account locale and product generation,
so this module aims to normalize several likely column naming variants.
"""

from __future__ import annotations

import ast
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional

import pandas as pd


STAGE_ALIASES = {
    "awake": "awake",
    "wake": "awake",
    "wakeup": "awake",
    "awakened": "awake",
    "light": "light",
    "lightsleep": "light",
    "light sleep": "light",
    "core": "light",
    "deep": "deep",
    "deepsleep": "deep",
    "deep sleep": "deep",
    "slow wave": "deep",
    "rem": "rem",
    "remsleep": "rem",
    "rem sleep": "rem",
    "rapid eye movement": "rem",
    "0": "awake",
    "1": "light",
    "2": "deep",
    "3": "rem",
    "4": "awake",
}


def _find_column(columns: Iterable[str], candidates: Iterable[str]) -> Optional[str]:
    canon = {c.strip().lower(): c for c in columns}
    for cand in candidates:
        if cand in canon:
            return canon[cand]
    return None


def _read_export_csv(csv_path: Path) -> pd.DataFrame:
    # sep=None lets pandas infer comma/tab/semicolon delimiters.
    return pd.read_csv(csv_path, sep=None, engine="python", encoding="utf-8-sig")


def _normalize_stage(value: object) -> Optional[str]:
    if value is None:
        return None
    key = str(value).strip().lower().replace("_", " ")
    key = " ".join(key.split())
    return STAGE_ALIASES.get(key)


def _coerce_local_datetime(series: pd.Series, tz_mode: str) -> pd.Series:
    # First try preserving timezone info; fallback to UTC-normalized parse when
    # source contains mixed offsets (e.g. +01:00 and +02:00 across DST).
    try:
        parsed = pd.to_datetime(series, errors="coerce", utc=False)
    except ValueError:
        parsed = pd.to_datetime(series, errors="coerce", utc=True)
    if tz_mode != "local":
        if getattr(parsed.dt, "tz", None) is not None:
            return parsed.dt.tz_convert("UTC").dt.tz_localize(None)
        return parsed

    # Local alignment requested.
    local_tz = datetime.now().astimezone().tzinfo
    if getattr(parsed.dt, "tz", None) is not None:
        return parsed.dt.tz_convert(local_tz).dt.tz_localize(None)
    return parsed


def _parse_array_field(value: object) -> list[object]:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return []
    if isinstance(value, (list, tuple)):
        return list(value)

    text = str(value).strip()
    if not text:
        return []

    try:
        parsed = ast.literal_eval(text)
    except (ValueError, SyntaxError):
        # Fallback for malformed values like "1,2,3"
        if "," in text:
            return [p.strip() for p in text.split(",") if p.strip()]
        return [text]

    if isinstance(parsed, (list, tuple)):
        return list(parsed)
    return [parsed]


def _expand_duration_value_numeric(
    df: pd.DataFrame,
    start_col: str,
    duration_col: str,
    value_col: str,
    tz_mode: str,
    value_name: str,
) -> pd.DataFrame:
    starts = _coerce_local_datetime(df[start_col], tz_mode)
    rows: list[tuple[pd.Timestamp, float]] = []

    for start, durations_raw, values_raw in zip(starts, df[duration_col], df[value_col]):
        if pd.isna(start):
            continue

        durations = _parse_array_field(durations_raw)
        values = _parse_array_field(values_raw)
        if not durations or not values:
            continue

        n = min(len(durations), len(values))
        t = pd.Timestamp(start)
        for i in range(n):
            try:
                dur_sec = float(durations[i])
                val = float(values[i])
            except (TypeError, ValueError):
                continue
            if dur_sec <= 0:
                continue
            t_mid = t + pd.to_timedelta(dur_sec / 2.0, unit="s")
            rows.append((t_mid, val))
            t = t + pd.to_timedelta(dur_sec, unit="s")

    if not rows:
        raise ValueError("No valid numeric rows parsed from start/duration/value format.")

    out = pd.DataFrame(rows, columns=["timestamp_local", value_name])
    out = out.sort_values("timestamp_local").reset_index(drop=True)
    return out


def _expand_duration_value_format(
    df: pd.DataFrame,
    start_col: str,
    duration_col: str,
    value_col: str,
    tz_mode: str,
) -> pd.DataFrame:
    starts = _coerce_local_datetime(df[start_col], tz_mode)
    rows: list[tuple[pd.Timestamp, str]] = []

    for start, durations_raw, values_raw in zip(starts, df[duration_col], df[value_col]):
        if pd.isna(start):
            continue

        durations = _parse_array_field(durations_raw)
        values = _parse_array_field(values_raw)
        if not durations or not values:
            continue

        n = min(len(durations), len(values))
        t = pd.Timestamp(start)
        for i in range(n):
            try:
                dur_sec = float(durations[i])
            except (TypeError, ValueError):
                continue
            if dur_sec <= 0:
                continue

            stage = _normalize_stage(values[i])
            t_end = t + pd.to_timedelta(dur_sec, unit="s")
            if stage:
                mins = pd.date_range(
                    t.floor("min"),
                    t_end.floor("min"),
                    freq="1min",
                    inclusive="left",
                )
                if len(mins):
                    rows.extend((m, stage) for m in mins)
            t = t_end

    if not rows:
        raise ValueError("No valid rows parsed from start/duration/value format.")

    out = pd.DataFrame(rows, columns=["timestamp_local", "stage_label"])
    out = out.drop_duplicates(subset=["timestamp_local"], keep="last")
    out = out.sort_values("timestamp_local").reset_index(drop=True)
    return out


def load_withings_sleep(csv_path: Path, tz_mode: str = "local") -> pd.DataFrame:
    """Load a Withings CSV export into a normalized minute-level stage table.

    Returns a DataFrame with columns:
      - timestamp_local (naive datetime in local tz if tz_mode=local)
      - stage_label in {awake, light, deep, rem}
    """

    csv_path = Path(csv_path)
    df = _read_export_csv(csv_path)
    if df.empty:
        raise ValueError(f"Withings file is empty: {csv_path}")

    cols = list(df.columns)
    start_col = _find_column(
        cols,
        ["start", "start time", "start datetime", "from", "begin", "date from"],
    )
    duration_col = _find_column(cols, ["duration", "durations"]) 
    value_col = _find_column(cols, ["value", "values", "sleep value", "state value", "stage value"])

    # Withings tracker raw export commonly uses:
    # start,duration,value
    # where duration/value are arrays of per-segment seconds + stage codes.
    if start_col and duration_col and value_col:
        out = _expand_duration_value_format(
            df,
            start_col=start_col,
            duration_col=duration_col,
            value_col=value_col,
            tz_mode=tz_mode,
        )
        if out.empty:
            raise ValueError("No valid stage rows after parsing duration/value format.")
        return out

    stage_col = _find_column(
        cols,
        [
            "sleep state",
            "sleep stage",
            "state",
            "stage",
            "status",
            "sleepstatus",
            "sleep_status",
        ],
    )
    if not stage_col:
        raise ValueError(
            "Could not find a stage/state column in Withings export. "
            f"Columns seen: {cols}"
        )

    end_col = _find_column(
        cols,
        ["end", "end time", "end datetime", "to", "finish", "date to"],
    )
    timestamp_col = _find_column(
        cols,
        [
            "timestamp",
            "time",
            "datetime",
            "date",
            "startdate",
            "start_date",
            "start time",
        ],
    )

    normalized = []
    if start_col and end_col:
        starts = _coerce_local_datetime(df[start_col], tz_mode)
        ends = _coerce_local_datetime(df[end_col], tz_mode)
        stages = df[stage_col].map(_normalize_stage)

        for start, end, stage in zip(starts, ends, stages):
            if pd.isna(start) or pd.isna(end) or not stage:
                continue
            if end <= start:
                continue
            mins = pd.date_range(start.floor("min"), end.floor("min"), freq="1min", inclusive="left")
            if len(mins) == 0:
                continue
            normalized.append(
                pd.DataFrame({"timestamp_local": mins, "stage_label": stage})
            )

        if not normalized:
            raise ValueError("No usable rows found in start/end stage format.")
        out = pd.concat(normalized, ignore_index=True)
    elif timestamp_col:
        stamps = _coerce_local_datetime(df[timestamp_col], tz_mode)
        stages = df[stage_col].map(_normalize_stage)
        out = pd.DataFrame({"timestamp_local": stamps, "stage_label": stages})
        out = out.dropna(subset=["timestamp_local", "stage_label"])
    else:
        raise ValueError(
            "Could not infer timestamp columns from Withings export. "
            f"Columns seen: {cols}"
        )

    out = out.sort_values("timestamp_local")
    out = out.drop_duplicates(subset=["timestamp_local"], keep="last")
    out = out.reset_index(drop=True)
    if out.empty:
        raise ValueError("No valid stage rows after normalization.")
    return out


def load_withings_hr(csv_path: Path, tz_mode: str = "local") -> pd.DataFrame:
    """Load Withings HR export into a normalized table.

    Returns columns:
      - timestamp_local
      - hr_bpm
    """

    csv_path = Path(csv_path)
    df = _read_export_csv(csv_path)
    if df.empty:
        raise ValueError(f"Withings HR file is empty: {csv_path}")

    cols = list(df.columns)
    start_col = _find_column(cols, ["start", "start time", "time", "timestamp", "datetime"])
    duration_col = _find_column(cols, ["duration", "durations"])
    value_col = _find_column(cols, ["value", "values", "heart rate", "hr", "bpm"])

    if start_col and duration_col and value_col:
        out = _expand_duration_value_numeric(
            df,
            start_col=start_col,
            duration_col=duration_col,
            value_col=value_col,
            tz_mode=tz_mode,
            value_name="hr_bpm",
        )
    elif start_col and value_col:
        stamps = _coerce_local_datetime(df[start_col], tz_mode)
        vals = pd.to_numeric(df[value_col], errors="coerce")
        out = pd.DataFrame({"timestamp_local": stamps, "hr_bpm": vals})
    else:
        raise ValueError(
            "Could not infer HR columns from Withings file. "
            f"Columns seen: {cols}"
        )

    out = out.dropna(subset=["timestamp_local", "hr_bpm"])
    out = out.sort_values("timestamp_local").reset_index(drop=True)
    if out.empty:
        raise ValueError("No valid HR rows after normalization.")
    return out


def load_withings_nights_summary(csv_path: Path, tz_mode: str = "local") -> pd.DataFrame:
    """Load Withings sleep.csv nightly summaries if available."""

    csv_path = Path(csv_path)
    df = _read_export_csv(csv_path)
    if df.empty:
        raise ValueError(f"Withings sleep summary file is empty: {csv_path}")

    cols = list(df.columns)
    from_col = _find_column(cols, ["from", "start", "start time"])
    to_col = _find_column(cols, ["to", "end", "end time"])
    if not from_col or not to_col:
        raise ValueError(
            "Could not infer nightly interval columns from sleep summary. "
            f"Columns seen: {cols}"
        )

    out = pd.DataFrame()
    out["from_local"] = _coerce_local_datetime(df[from_col], tz_mode)
    out["to_local"] = _coerce_local_datetime(df[to_col], tz_mode)

    key_map = {
        "light (s)": "light_s",
        "deep (s)": "deep_s",
        "rem (s)": "rem_s",
        "awake (s)": "awake_s",
        "average heart rate": "avg_hr",
        "heart rate (min)": "min_hr",
        "heart rate (max)": "max_hr",
    }
    canon_cols = {c.strip().lower(): c for c in cols}
    for src_key, dst_key in key_map.items():
        if src_key in canon_cols:
            out[dst_key] = pd.to_numeric(df[canon_cols[src_key]], errors="coerce")

    out = out.dropna(subset=["from_local", "to_local"]).copy()
    out["duration_min"] = (out["to_local"] - out["from_local"]).dt.total_seconds() / 60.0
    for src in ["light_s", "deep_s", "rem_s", "awake_s"]:
        if src in out.columns:
            out[src.replace("_s", "_min")] = out[src] / 60.0

    out = out.sort_values("from_local").reset_index(drop=True)
    if out.empty:
        raise ValueError("No valid nightly rows after normalization.")
    return out
