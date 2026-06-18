# J — Dashboard

**When:** After core analysis; refine after phase I

---

## Goal

Let someone explore key results **without** reading the full notebook.

## Implementation

Streamlit app: [`app/app.py`](../app/app.py)

Run instructions: [`app/README.md`](../app/README.md)

## Data source

- `analysis_data/analysis_base.csv` — joined current valuation, scale, profitability, and annual reported financial metrics

## Current views

| View | Status |
|------|--------|
| KPI row (revenue, net income) | Done |
| Scale chart (latest revenue and net income) | Done |
| Valuation chart (P/S, trailing P/E, forward P/E) | Done |
| Growth trajectory (YoY % change) | Done |
| Comparison table | Done |
| Strategy calculator and research summary | Done |

## Optional later enhancements

- Sidebar filters (company, metric, fiscal-year range)
- Revenue and net income trend lines
- Screenshot export for presentation

## Deliverable

- [x] Streamlit dashboard in `app/app.py`
- [x] Run instructions in `app/README.md`
- [ ] Screenshot backup for presentation

## Note

Streamlit is **presentation** — analysis logic stays in the notebook and prepared CSV analysis data.

## Next step

→ [K — Presentation](K-presentation.md)
