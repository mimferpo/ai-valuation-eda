# Data fetch

Pull Yahoo Finance data into `raw_data/{FOLDER}/`.

Edit `fetch_config.json` to change **what** gets pulled. Edit `fetch.py` only when the download behavior itself needs to change.

## Files

| File | Role |
|------|------|
| `fetch_config.json` | Tickers and output specs |
| `fetch.py` | Pull engine — reads config and writes raw files |
| `YFINANCE_OPTIONS.md` | Guide for discovering and adding more yfinance outputs |

## Run

From the project root:

```bash
python data_fetch/fetch.py
```

Each run fully refreshes `raw_data/`: the folder is deleted and recreated before new files are downloaded.

Flow:

```text
data_fetch/fetch_config.json
        ↓
data_fetch/fetch.py
        ↓
raw_data/{TICKER}/
```

## Current output

Active symbols are `MSFT` and `GOOGL`. The top-level `outputs` list pulls only the two raw sources needed for the final analysis.

| File | One row is… |
|------|-------------|
| `financials.csv` | Account line; columns = fiscal years |
| `info.json` | Key-value company snapshot for market cap, P/E, P/S, revenue, margin, and price |

## Config shape

Use simple ticker strings for the current project scope. Only these top-level keys control the current run:

```json
{
  "sleep_seconds": 1,
  "symbols": ["MSFT", "GOOGL"],
  "outputs": [
    {"kind": "csv_attr", "attr": "financials"},
    {"kind": "json_attr", "attr": "info", "filename": "info.json"}
  ]
}
```

For a custom folder, a symbol can also be an object such as `{"ticker": "MSFT", "folder": "Microsoft"}`.

## Add More Outputs

See [`YFINANCE_OPTIONS.md`](YFINANCE_OPTIONS.md) before adding new fields to `fetch_config.json`.


