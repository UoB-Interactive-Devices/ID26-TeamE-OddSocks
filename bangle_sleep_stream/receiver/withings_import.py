"""Flexible parser for Withings sleep exports.

The exporter format can vary by account locale and product generation,
so this module aims to normalize several likely column naming variants.
"""

from __future__ import annotations

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


def _normalize_stage(value: object) -> Optional[str]:
    if value is None:
        return None
    key = str(value).strip().lower().replace("_", " ")
    key = " ".join(key.split())
    return STAGE_ALIASES.get(key)


def _coerce_local_datetime(series: pd.Series, tz_mode: str) -> pd.Series:
    # First parse while preserving timezone if present.
    parsed = pd.to_datetime(series, errors="coerce", utc=False)
    if tz_mode != "local":
        if getattr(parsed.dt, "tz", None) is not None:
            return parsed.dt.tz_convert("UTC").dt.tz_localize(None)
        return parsed

    # Local alignment requested.
    local_tz = datetime.now().astimezone().tzinfo
    if getattr(parsed.dt, "tz", None) is not None:
        return parsed.dt.tz_convert(local_tz).dt.tz_localize(None)
    return parsed


def load_withings_sleep(csv_path: Path, tz_mode: str = "local") -> pd.DataFrame:
    """Load a Withings CSV export into a normalized minute-level stage table.

    Returns a DataFrame with columns:
      - timestamp_local (naive datetime in local tz if tz_mode=local)
      - stage_label in {awake, light, deep, rem}
    """

    csv_path = Path(csv_path)
    df = pd.read_csv(csv_path)
    if df.empty:
        raise ValueError(f"Withings file is empty: {csv_path}")

    cols = list(df.columns)
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

    start_col = _find_column(
        cols,
        ["start", "start time", "start datetime", "from", "begin", "date from"],
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
