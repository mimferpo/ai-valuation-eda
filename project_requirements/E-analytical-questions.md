# E — Join into analysis base

**EDA guide:** Analytical question · Section 3 evidence plan  
**When:** After clean data exists — **before** building most charts

---

## Goal

Turn the business question into one **specific, answerable** analytical question and define the evidence columns that support it.

## Main Analytical Question

> Which AI-exposed megacap looks more reasonably valued relative to revenue and profitability: Microsoft or Google?

## Evidence Metrics

Keep these as columns and metrics for the same question, not as separate main questions.

- **Valuation:** `price_to_sales`, `trailingPE`, `forwardPE` from `analysis_base.csv`
- **Profitability:** `profitMargins` from `analysis_base.csv`; `Net Income` metric rows from `analysis_base.csv`
- **Scale:** `info_total_revenue` from `analysis_base.csv`; `Total Revenue` metric rows from `analysis_base.csv`

## Data Approach

- Use the Phase E joined base: `analysis_data/analysis_base.csv`.
- Treat the Phase D files, `analysis_data/merged_info.csv` and `analysis_data/merged_financials.csv`, as the source exports used to build that base.
- Keep the project scope to MSFT vs GOOGL.
- Filter `analysis_base.csv` to `Total Revenue` and `Net Income` metric rows for the core profitability and scale evidence.

## Weak vs strong

| Weak | Strong |
|------|--------|
| “Valuation” | “Use P/S, trailing P/E, and forward P/E as valuation evidence for the MSFT vs GOOGL question.” |
| “Profitability” | “Use profit margin and net income to judge whether a higher multiple is supported by profitability.” |

## Evidence Checklist

- Compare current P/S, trailing P/E, and forward P/E side by side.
- Compare current profit margin and latest reported net income.
- Compare current total revenue and latest reported total revenue.
- Review available fiscal-year trends for `Total Revenue` and `Net Income`.
- Combine valuation, profitability, and scale in the final interpretation.

## Deliverable

Notebook Section 3 should state the main analytical question once, then list the evidence metrics and prepared Phase E analysis-base approach.

## Flexibility

If a metric is missing or unreliable, say what extra data you would need and keep the conclusion cautious.

## Next step

→ [F — Descriptive statistics](F-descriptive-statistics.md)
