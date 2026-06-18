# SQL folder

Manual DuckDB SQL files for phases B–E.

Raw inputs come from [`data_fetch/`](../data_fetch/) into `raw_data/`. Final analysis CSVs are written to `analysis_data/`.

## Files

| File | Role |
|------|------|
| [`phase-b.sql`](phase-b.sql) | Inspect raw grain |
| [`phase-c.sql`](phase-c.sql) | Validate schema/counts |
| [`phase-d.sql`](phase-d.sql) | Unpivot & merge metrics |
| [`phase-e.sql`](phase-e.sql) | Join into analysis base |

## Run

Open a phase file in DuckDB / the VS Code DuckDB extension and run the SQL manually.

Recommended order:

```text
phase-b.sql   # inspect raw grain
phase-c.sql   # validate schema/counts
phase-d.sql   # unpivot & merge metrics
phase-e.sql   # join into analysis base
```

Phase F descriptive statistics are completed in `notebooks/main.ipynb`. Phase G–H charts are in `app/app.py`. Both load the prepared `analysis_data/analysis_base.csv` produced by Phase E.

## Refresh Rule

`phase-d.sql` overwrites the two generated Phase D CSVs in `analysis_data/` when rerun:

```text
analysis_data/merged_financials.csv
analysis_data/merged_info.csv
```

`phase-e.sql` then joins those files and overwrites:

```text
analysis_data/analysis_base.csv
```

## Final Scope

The SQL is intentionally narrow: MSFT vs GOOGL, using only `financials.csv` and `info.json` as raw inputs.
