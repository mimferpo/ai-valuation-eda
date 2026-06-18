-- Phase C — Quality audit (MSFT)
-- Run manually in DuckDB / VS Code DuckDB extension.
-- Validate schema, row count, nulls, and duplicates before Phase D.

-- INDEX
-- | Step | Line | What it does |
-- | C1   | ~15  | DESCRIBE financials schema/types |
-- | C2   | ~20  | DESCRIBE info schema/types |
-- | C3   | ~25  | Count financials rows |
-- | C4   | ~31  | Count null metric labels |
-- | C5   | ~37  | Find duplicate financial metric labels |
-- | C6   | ~42  | Confirm one info row |

-- C1: financials column names + types (schema check — not row count)
--     Action: DESCRIBE financials CSV to confirm fiscal-year columns are present
--     FINDING: column0 = metric label; year columns become long rows in Phase D
DESCRIBE SELECT * FROM read_csv_auto('raw_data/MSFT/financials.csv');

-- C2: info column names + types
--     Action: DESCRIBE info JSON fields used for current valuation and profitability ratios
--     FINDING: selected fields feed merged_info.csv in Phase D
DESCRIBE SELECT * FROM read_json('raw_data/MSFT/info.json');

-- C3: financials row count
--     Action: COUNT(*) on financials to verify useful statement coverage
SELECT COUNT(*) AS n_rows
FROM read_csv_auto('raw_data/MSFT/financials.csv');

-- C4: financials missing metric labels
--     Action: count null labels; rows without metric names cannot be interpreted
SELECT COUNT(*) - COUNT(column0) AS null_metric_labels
FROM read_csv_auto('raw_data/MSFT/financials.csv');

-- C5: duplicate financial metric labels (empty result = good)
--     Action: GROUP BY column0 HAVING COUNT > 1 — any rows returned need review
SELECT column0 AS metric FROM read_csv_auto('raw_data/MSFT/financials.csv')
GROUP BY column0 HAVING COUNT(*) > 1;

-- C6: info snapshot row count
--     Action: confirm info.json reads as a single company snapshot row
SELECT COUNT(*) AS info_rows
FROM read_json('raw_data/MSFT/info.json');

-- Phase B carry-over: financials are wide and info is one-row JSON; merge both in Phase D
