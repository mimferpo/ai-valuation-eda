# H — Time series & correlation

**EDA guide:** Section 5 — Time series & correlation analysis  
**When:** After main visual exploration (phase G)

---

## Goal

Study **how annual fundamentals evolve over time** and how the available evidence metrics relate to valuation.

## Tasks

- [ ] Use the **date column** `fiscal_year_end`
- [ ] Work at fiscal-year grain; note that no daily price series is part of the final analysis
- [ ] Plot **rolling average** or multi-year trend (e.g. 3-period rolling mean of margin)
- [ ] Describe **at least one pattern** over time (trend up/down, divergence between firms)
- [ ] **Seasonality** — with annual fundamentals, discuss fiscal-year effects instead
- [ ] **Correlation analysis** — treat as exploratory because two companies and annual rows limit statistical power
- [ ] Compare valuation evidence manually: P/S and P/E vs revenue scale, profit margin, and net income
- [ ] Keep analysis within the prepared Phase E base: `analysis_data/analysis_base.csv`

## Main variable candidates

- `price_to_sales`, `trailingPE`, `forwardPE` (valuation)
- `profitMargins` and `Net Income` (profitability)
- `totalRevenue` and `Total Revenue` (scale)

## Deliverable

- YoY change table in `notebooks/main.ipynb`
- Optional trend charts can be added later in `app/app.py`

## Flexibility

Pure annual fundamentals have weak "seasonality" — use fiscal trends and rolling windows, and clearly state that price history is outside the final analysis-data scope.

## Next step

→ [I — Conclusions](I-conclusions.md)
