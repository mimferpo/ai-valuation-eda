# F — Descriptive statistics

**EDA guide:** Section 3 — Descriptive statistics  
**When:** After the question and evidence plan are written (phase E)

---

## Goal

Summarize the evidence metrics numerically before answering the **one main analytical question**.

Phase F is completed in `notebooks/main.ipynb`, not in a separate SQL file. This keeps the summary tables, outputs, and interpretation together. Load `analysis_data/analysis_base.csv`, which is exported by `sql/phase-e.sql`.

## Tasks

- [ ] Central tendency & dispersion for key numerics (`mean`, `median`, `std`, quartiles)
- [ ] `.describe()` on revenue, net income, margins, P/E, and P/S
- [ ] `groupby` comparisons — e.g. by `symbol` and by fiscal year
- [ ] Comment on the limits of descriptive stats with two companies
- [ ] Peer view — direct MSFT vs GOOGL P/S and P/E comparison
- [ ] State the Phase E question once, then describe valuation, profitability, and scale evidence

## Suggested groupbys

- Latest revenue and net income by `symbol`
- Current P/S, trailing P/E, and forward P/E by `symbol`
- Revenue by `symbol` and `fiscal_year_end`

## Deliverable

- Summary statistics table(s)
- Short interpretation paragraphs (not just numbers)
- Evidence metric summary for valuation, profitability, and scale

## Flexibility

Use median when distributions are skewed; say why.

## Next step

→ [G — Visual exploration](G-visual-exploration.md)
