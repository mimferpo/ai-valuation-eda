-- Phase D — Merge MSFT and GOOGL into two final analysis_data
-- Run manually in DuckDB / VS Code DuckDB extension.
-- Creates:
--   1. analysis_data/merged_financials.csv from financials.csv
--   2. analysis_data/merged_info.csv from info.json

-- INDEX
-- | Step | What it does |
-- | D0   | Optional cleanup for old generated CSVs |
-- | D1   | CREATE and COPY merged financials |
-- | D2   | CREATE and COPY merged info snapshot |

-- =============================================================================
-- D0: OUTPUT REFRESH TOGGLE - replace generated Phase D CSV files
--     Toggle ON: keep OVERWRITE_OR_IGNORE true in the COPY statements below.
--     Toggle OFF: remove OVERWRITE_OR_IGNORE true if you want DuckDB to error
--                 when a target CSV already exists.
--     Purpose: prevent stale analysis_data files from remaining between reruns
--              without manually deleting files.
-- =============================================================================

-- =============================================================================
-- D1: FINANCIALS - MSFT and GOOGL, all metrics, long format
--     Action: unpivot wide CSV -> symbol | metric | fiscal_year_end | amount
-- =============================================================================

CREATE OR REPLACE TABLE financial_metrics_all AS
SELECT
    symbol,
    metric,
    TRY_CAST(fiscal_year_end AS DATE) AS fiscal_year_end,
    TRY_CAST(amount AS DOUBLE)         AS amount
FROM (
    SELECT * FROM (
        UNPIVOT (SELECT 'MSFT' AS symbol, column0 AS metric, * EXCLUDE (column0)
                 FROM read_csv_auto('raw_data/MSFT/financials.csv'))
        ON COLUMNS(* EXCLUDE (symbol, metric)) INTO NAME fiscal_year_end VALUE amount
    )
    UNION ALL
    SELECT * FROM (
        UNPIVOT (SELECT 'GOOGL' AS symbol, column0 AS metric, * EXCLUDE (column0)
                 FROM read_csv_auto('raw_data/GOOGL/financials.csv'))
        ON COLUMNS(* EXCLUDE (symbol, metric)) INTO NAME fiscal_year_end VALUE amount
    )
) u
WHERE amount IS NOT NULL;

COPY financial_metrics_all TO 'analysis_data/merged_financials.csv' (
    HEADER,
    DELIMITER ',',
    OVERWRITE_OR_IGNORE true
);


-- =============================================================================
-- D2: INFO - MSFT and GOOGL, one snapshot row per company
--     Action: read_json per ticker; UNION ALL into a company-info table
-- =============================================================================

CREATE OR REPLACE TABLE info_all AS
SELECT 'MSFT' AS symbol, marketCap, trailingPE, forwardPE,
       priceToSalesTrailing12Months AS price_to_sales, totalRevenue, profitMargins, currentPrice
FROM read_json('raw_data/MSFT/info.json')
UNION ALL
SELECT 'GOOGL' AS symbol, marketCap, trailingPE, forwardPE,
       priceToSalesTrailing12Months AS price_to_sales, totalRevenue, profitMargins, currentPrice
FROM read_json('raw_data/GOOGL/info.json');

COPY info_all TO 'analysis_data/merged_info.csv' (
    HEADER,
    DELIMITER ',',
    OVERWRITE_OR_IGNORE true
);
