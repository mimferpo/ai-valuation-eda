# D — Unpivot & merge metrics

**EDA guide:** Section 2 (part 2) — cleaning & feature engineering  
**When:** After quality audit (phase C)

---

## Goal

Produce a **clean, analysis-ready** MSFT vs GOOGL table and at least **one engineered feature**.

## Tasks

- [ ] Parse date columns (`fiscal_year_end`)
- [ ] Standardize text (`symbol`, `company_name` — strip, consistent casing)
- [ ] Handle missing values — document every decision (drop, keep, impute, flag)
- [ ] Handle outliers — remove, cap, or keep with justification
- [ ] Create **≥ 1 engineered feature**, e.g.:
  - `net_margin` = net_income / revenue
  - `is_profitable` or `profit_status`
  - `market_cap_to_revenue` or `ps_gap` comparing current P/S between MSFT and GOOGL
- [ ] Use Phase D analysis_data: `analysis_data/merged_financials.csv` and `analysis_data/merged_info.csv`
- [ ] Run `sql/phase-d.sql` manually; it overwrites the two Phase D CSVs in `analysis_data/`
- [ ] Run `sql/phase-e.sql` manually after Phase D when the joined notebook input needs to be refreshed

## Cleaning log (markdown)

For each change, write:

```text
Issue: …
Action: …
Reason: …
```

## Deliverable

- Clean `DataFrame` used in all later phases
- Written summary of cleaning decisions
- Clean source exports from Phase D, then joined through Phase E as `analysis_data/analysis_base.csv` for notebook and dashboard use

## Flexibility

Engineered features can grow in F or H — but you need **at least one** here to meet the guide.

## Next step

→ [E — Join into analysis base](E-analytical-questions.md)
