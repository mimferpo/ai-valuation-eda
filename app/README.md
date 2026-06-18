# Streamlit dashboard

Interactive dashboard for the MSFT vs GOOGL valuation comparison.

## Run

```bash
conda activate ai-valuation-eda
streamlit run app/app.py
```

## Data source

Loads `analysis_data/analysis_base.csv`, exported by `sql/phase-e.sql`.

## What it shows

1. Latest revenue and net income (scale)
2. Valuation multiples (P/S, trailing P/E, forward P/E)
3. Growth trajectory (YoY % change)
4. Side-by-side comparison table
5. Strategy calculator and research summary

Analysis tables live in `notebooks/main.ipynb`. This app is the visual presentation layer.

## Refresh data

```bash
python run_pipeline.py
```

The `run_pipeline.py` script automatically runs the fetch and SQL transformations. You can also trigger this directly from the Streamlit sidebar.
