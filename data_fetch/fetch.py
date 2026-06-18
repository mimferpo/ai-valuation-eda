#!/usr/bin/env python3
"""Download raw yfinance data — engine; config in fetch_config.json."""

from __future__ import annotations

import json
import shutil
import time
from importlib import import_module
from pathlib import Path
from typing import Any

FETCH_DIR = Path(__file__).resolve().parent
CONFIG_PATH = FETCH_DIR / "fetch_config.json"
DATA_DIR = FETCH_DIR.parent / "raw_data"


def reset_directory(path: Path) -> None:
    """Remove and recreate a generated output directory."""
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def load_config() -> dict[str, Any]:
    """Read fetch_config.json."""
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def save_config(config: dict[str, Any]) -> None:
    """Write fetch_config.json."""
    CONFIG_PATH.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")


def outputs_for_symbol(
    entry: str | dict[str, Any],
    config: dict[str, Any] | None = None,
) -> list[dict[str, str]]:
    """Resolve output specs for one symbol."""
    cfg = config if config is not None else load_config()
    if isinstance(entry, dict) and "outputs" in entry:
        return entry["outputs"]
    return cfg["outputs"]


def symbol_and_folder(entry: str | dict[str, Any]) -> tuple[str, str]:
    """Return the ticker symbol and output folder for one config entry."""
    if isinstance(entry, str):
        return entry, entry
    ticker = str(entry["ticker"])
    return ticker, str(entry.get("folder", ticker))


def save_csv(obj: Any, path: Path) -> None:
    """Write a non-empty DataFrame or Series to CSV."""
    if obj is None:
        return
    pd = import_module("pandas")
    if isinstance(obj, (pd.DataFrame, pd.Series)) and obj.empty:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    obj.to_csv(path, header=True)


def save_json_file(obj: Any, path: Path) -> None:
    """Write non-empty dict-like data to JSON."""
    if not obj:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=str), encoding="utf-8")


def resolve_output(ticker: Any, spec: dict[str, str]) -> Any:
    """Return yfinance data for one output spec."""
    kind = spec["kind"]
    if kind == "csv_attr":
        return getattr(ticker, spec["attr"])
    if kind == "history":
        kwargs: dict[str, str] = {}
        if spec.get("period"):
            kwargs["period"] = spec["period"]
        if spec.get("interval"):
            kwargs["interval"] = spec["interval"]
        if spec.get("start"):
            kwargs["start"] = spec["start"]
        if spec.get("end"):
            kwargs["end"] = spec["end"]
        return ticker.history(**kwargs)
    if kind == "json_attr":
        return getattr(ticker, spec["attr"])
    raise ValueError(f"Unknown output kind: {kind}")


def output_path(out_dir: Path, spec: dict[str, str]) -> Path:
    """Resolve disk path for one output spec."""
    if spec["kind"] == "csv_attr":
        return out_dir / spec.get("filename", f"{spec['attr']}.csv")
    return out_dir / spec["filename"]


def fetch_symbol(ticker_symbol: str, folder: str, outputs: list[dict[str, str]]) -> None:
    out_dir = DATA_DIR / folder
    out_dir.mkdir(parents=True, exist_ok=True)
    yf = import_module("yfinance")
    ticker = yf.Ticker(ticker_symbol)

    for spec in outputs:
        path = output_path(out_dir, spec)
        data = resolve_output(ticker, spec)
        if spec["kind"] == "json_attr":
            save_json_file(data, path)
        else:
            save_csv(data, path)

    label = f"{ticker_symbol}→{folder}" if folder != ticker_symbol else ticker_symbol
    print(f"{label}: done")


def main() -> None:
    config = load_config()
    symbols = config["symbols"]
    sleep = config["sleep_seconds"]

    reset_directory(DATA_DIR)

    for entry in symbols:
        ticker, folder = symbol_and_folder(entry)
        outputs = outputs_for_symbol(entry, config)
        fetch_symbol(ticker, folder, outputs)
        time.sleep(sleep)

    print(f"\nDone. Output → {DATA_DIR}")


if __name__ == "__main__":
    main()
