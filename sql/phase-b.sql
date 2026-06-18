-- Phase B — Import & first look (MSFT grain sample; same shape for GOOGL)
-- Run manually in DuckDB / VS Code DuckDB extension.
-- Preview raw CSV grain before merge/unpivot in Phase D.

-- INDEX
-- | Step | Line | What it does |
-- | B1   | ~15  | Sample MSFT financials grain |
-- | B2   | ~20  | Sample MSFT info snapshot |

-- B1: financials — what is one row?
--     Action: sample 5 rows from MSFT financials to inspect wide-table layout
--     FINDING: wide table — column0 = metric name; other cols = fiscal year-end (2022–2026)
--              1 row = 1 income-statement line item
--              NULL on 2026 unusual-items & some 2022 cols = expected gaps, not fetch error
SELECT * FROM read_csv_auto('raw_data/MSFT/financials.csv') LIMIT 5;

-- B2: info — what is one row?
--     Action: sample the one-row MSFT company snapshot used for valuation ratios
--     FINDING: 1 row = current market cap, P/E, P/S, revenue, margin, and price fields
SELECT * FROM read_json('raw_data/MSFT/info.json') LIMIT 5;

-- Next (Phase D): rename column0 -> metric; unpivot year columns to long format
