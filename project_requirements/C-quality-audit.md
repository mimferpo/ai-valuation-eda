# C — Validate schema/counts

**EDA guide:** Section 2 (part 1) — identify issues before cleaning  
**When:** After initial import (phase B)

---

## Goal

Find data quality problems **before** you trust any chart or statistic.

## Tasks

- [ ] **Missing values** — per column; which matter for your question?
- [ ] **Duplicates** — same company + same financial metric twice?
- [ ] **Data types** — are dates parsed? are numbers stored as strings?
- [ ] **Consistency** — symbol naming, currency, fiscal year alignment
- [ ] **Expected gaps** — missing ratio fields in `info.json` or blank fiscal-year cells in `financials.csv`
- [ ] **Outliers (first pass)** — unusually large revenue, net income, P/E, or P/S values; flag for phase D
- [ ] **Coverage** — how many fiscal years per company?

## Questions to answer in markdown

| Check | Your notes |
|-------|------------|
| Rows with missing revenue or net income? | |
| Companies with &lt; 3 fiscal years? | |
| Missing `trailingPE`, `price_to_sales`, or `profitMargins` in `info.json`? | |
| Any duplicate keys? | |

## Deliverable

A short **audit table** or bullet list in the notebook: issue → severity → planned action (fix in D / keep / exclude).

## Flexibility

Not every null should be filled. If yfinance omits a current ratio field, document whether it affects the MSFT vs GOOGL answer.

## Next step

→ [D — Unpivot & merge metrics](D-clean-and-engineer.md)
