# yfinance Output Options

This guide explains how `data_fetch/fetch_config.json` maps to `yfinance`, and how to discover more outputs later.

## Current Config

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

Meaning:

| Config key | Meaning |
|------------|---------|
| `symbols` | Tickers passed to `yf.Ticker(...)` |
| `sleep_seconds` | Pause between tickers |
| `outputs` | List of yfinance data pulls to save |

## How `outputs` Works

`fetch.py` creates a ticker object:

```python
import yfinance as yf

ticker = yf.Ticker("MSFT")
```

Then each output spec tells `fetch.py` what to read from that object.

## `csv_attr`

Use `csv_attr` when the yfinance attribute returns a table-like object, usually a pandas `DataFrame`.

Example:

```json
{"kind": "csv_attr", "attr": "financials"}
```

This means:

```python
yf.Ticker("MSFT").financials
```

Default output filename:

```text
financials.csv
```

You can also choose a filename:

```json
{"kind": "csv_attr", "attr": "balance_sheet", "filename": "balance_sheet.csv"}
```

Common table attributes:

```text
financials
balance_sheet
cashflow
quarterly_financials
quarterly_balance_sheet
quarterly_cashflow
```

## `json_attr`

Use `json_attr` when the yfinance attribute returns dictionary-like data.

Example:

```json
{"kind": "json_attr", "attr": "info", "filename": "info.json"}
```

This means:

```python
yf.Ticker("MSFT").info
```

Common dictionary-like attribute:

```text
info
```

## `history`

Use `history` when you want price history, because it needs method arguments like `period` and `interval`.

Example:

```json
{"kind": "history", "period": "5y", "interval": "1d", "filename": "history.csv"}
```

This means:

```python
yf.Ticker("MSFT").history(period="5y", interval="1d")
```

Common periods:

```text
1y
2y
5y
10y
max
```

Common intervals:

```text
1d
1wk
1mo
```

## How to Discover More Options

Run this in Python:

```python
import yfinance as yf

ticker = yf.Ticker("MSFT")

for name in dir(ticker):
    if not name.startswith("_"):
        print(name)
```

Then test an attribute:

```python
ticker.balance_sheet
ticker.cashflow
ticker.info
```

Use this rule:

| Result type | Config kind |
|-------------|-------------|
| table / DataFrame | `csv_attr` |
| dictionary / JSON-like object | `json_attr` |
| method needing `period` / `interval` | `history` |

## Example: Add Balance Sheet

Change `outputs` to:

```json
"outputs": [
  {"kind": "csv_attr", "attr": "financials"},
  {"kind": "json_attr", "attr": "info", "filename": "info.json"},
  {"kind": "csv_attr", "attr": "balance_sheet"}
]
```

Then run:

```bash
python data_fetch/fetch.py
```

Expected new file:

```text
raw_data/MSFT/balance_sheet.csv
raw_data/GOOGL/balance_sheet.csv
```

## Important

Only add outputs that you actually plan to use in `sql/` or the notebook. Extra files make the project harder to explain.
