# B — Inspect raw grain

**EDA guide:** Section 1 — Dataset introduction & initial exploration  
**Prerequisite:** [A — Topic & data plan](A-topic-and-data-plan.md)  
**Status:** Complete  
**Next:** [C — Validate schema/counts](C-quality-audit.md)

---

## Goal

Fetch raw data, load into pandas, document **shape** and **grain** before cleaning or plotting.

Scope lives in **phase A** — reference it in the notebook intro; do not duplicate the basket table here.

---

## Workflow

| Step | Where | Action |
|------|-------|--------|
| 1 | `data_fetch/fetch.py` | `python data_fetch/fetch.py` — refreshes `raw_data/` → `raw_data/{TICKER}/` |
| 2 | `notebooks/main.ipynb` | Section 1 — load `financials.csv` and `info.json`; explore per comment legend |

**Notebook:** [`notebooks/main.ipynb`](../notebooks/main.ipynb) — single project notebook; Section 1 covers import and first look for MSFT and GOOGL.

**Fetch & raw files:** [`data_fetch/README.md`](../data_fetch/README.md) — canonical; do not duplicate here.

Do **not** re-fetch in the notebook. Explore order: **head → shape → info → describe**, then columns/dtypes/index/nulls/duplicates/value_counts.

Running `data_fetch/fetch.py` deletes and recreates `raw_data/`, so stale raw files from older ticker scopes do not remain.

---

## First-look cheatsheet

Files on disk only — no yfinance calls in the notebook.

| Step | Function | Purpose |
|------|----------|---------|
| 1 | `.head()` | Sample rows / grain |
| 2 | `.shape` | Row × column count |
| 3 | `.info()` | dtypes, non-null counts |
| 4 | `.describe()` | numeric summary |
| 5–10 | `.columns`, `.dtypes`, `.index`, `.isnull().sum()`, `.duplicated().sum()`, `.value_counts()` | See Section 1 checklist in notebook |

| File | One row is… |
|------|-------------|
| `financials.csv` | One account line; **columns** = fiscal years |
| `info.json` | One company snapshot with valuation, revenue, margin, and price fields |

---

## Tasks

- [x] `pip install -r requirements.txt`
- [x] `python data_fetch/fetch.py`
- [ ] Load `financials.csv` and `info.json` per symbol in Section 1
- [ ] Notebook intro — link phase A, private outliers, yfinance source
- [ ] Explore `financials` + `info` for MSFT and GOOGL; document grain, fiscal-year columns, and available ratio fields
- [ ] Note missing fields per symbol (carry to phase C)

## Deliverable

Markdown dataset introduction + explore output in [`notebooks/main.ipynb`](../notebooks/main.ipynb) Section 1.
