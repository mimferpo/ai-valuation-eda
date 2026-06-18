-- Phase E — Minimal analysis base for MSFT vs GOOGL
-- Purpose: join the Phase D analysis_data exports and save one analysis-base CSV.
-- Inputs:
--   1. analysis_data/merged_info.csv       -> one current company snapshot row per symbol
--   2. analysis_data/merged_financials.csv -> one row per symbol, metric, fiscal_year_end
-- Grain after join: one row per company + financial metric + fiscal year.

-- E1: CREATE TABLE — combine current valuation/profitability snapshot with annual financial metrics.
--     Join key: symbol, because both analysis_data identify companies with the same ticker column.
CREATE OR REPLACE TABLE phase_e_analysis_base AS
SELECT
    i.symbol,
    i.marketCap,
    i.trailingPE,
    i.forwardPE,
    i.price_to_sales,
    i.totalRevenue AS info_total_revenue,
    i.profitMargins,
    i.currentPrice,
    f.metric,
    f.fiscal_year_end,
    f.amount
FROM read_csv_auto('analysis_data/merged_info.csv') AS i
LEFT JOIN read_csv_auto('analysis_data/merged_financials.csv') AS f
    ON i.symbol = f.symbol;

-- E2: EXPORT — save the joined analysis base so the notebook can load one prepared CSV.
--     Toggle ON: keep OVERWRITE_OR_IGNORE true to replace the old joined output.
--     Toggle OFF: remove OVERWRITE_OR_IGNORE true if you want DuckDB to error
--                 when analysis_base.csv already exists.
COPY phase_e_analysis_base TO 'analysis_data/analysis_base.csv' (
    HEADER,
    DELIMITER ',',
    OVERWRITE_OR_IGNORE true
);

-- E3: PREVIEW — small check that the join returns both companies and financial rows.
SELECT *
FROM phase_e_analysis_base
ORDER BY symbol, metric, fiscal_year_end;

-- Phase E question design
-- Main analytical question:
-- Which AI-exposed megacap looks more reasonably valued relative to revenue and profitability: Microsoft or Google?

-- Supporting evidence columns, not separate main questions:
--   Valuation: price_to_sales, trailingPE, forwardPE from merged_info.
--   Profitability: profitMargins from merged_info; Net Income from merged_financials.
--   Scale: totalRevenue from merged_info; Total Revenue from merged_financials.
-- Notebook approach: load analysis_data/analysis_base.csv, then filter metric values
-- to 'Total Revenue' and 'Net Income' when needed.