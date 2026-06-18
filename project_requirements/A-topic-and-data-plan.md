# A — Topic & data plan

**EDA guide:** Before you start · mentor approval  
**Status:** Complete  
**Next:** [B — Inspect raw grain](B-import-and-first-look.md)

---

## Research goal

> Which AI-exposed megacap looks more reasonably valued relative to revenue and profitability: Microsoft or Google?

**Why:** Microsoft and Alphabet are both large public AI beneficiaries, but their valuation should be checked against **reported** revenue, profit, and market ratios — not hype alone.

**Rules:** Public data only · cite sources · not investment advice · mentor approved.

---

## AI stack (context)

```text
Chips / cloud (public)  →  Foundation models (mostly private)  →  Apps & infra (mixed)
```

This project narrows the public AI layer to two hyperscaler megacaps: Microsoft and Alphabet. Private model labs are documented as **outliers** below — important to the AI story, but no stock data on yfinance.

---

## In scope — 2 AI-exposed megacaps

AI is central to both companies' product and cloud narratives. The analysis compares valuation against revenue scale and profitability.

| Symbol | Company | Category |
|--------|---------|----------|
| MSFT | Microsoft | cloud |
| GOOGL | Alphabet | cloud |

---

## Out of scope — indirect public names

Other listed firms may be AI-exposed, but they are excluded so the project stays a simple MSFT vs GOOGL comparison.

| Symbol | Company | Why indirect |
|--------|---------|--------------|
| AI chipmakers | Public semiconductor firms | Excluded to avoid changing the comparison into a chip-vs-cloud story |
| Other hyperscalers and social platforms | Public megacaps with AI exposure | Excluded from the two-company comparison |
| Enterprise AI/software firms | Public software firms | Smaller/different business models than the two megacaps |
| INTC | Intel | Legacy PC/datacenter mix |
| TSM | Taiwan Semiconductor | Fab for all chips, not AI-specific |
| ARM | Arm | IP licensor; AI is one use case |
| ORCL | Oracle | Cloud AI push on legacy ERP/DB base |
| IBM | IBM | watsonx vs legacy services/hardware |
| CRM | Salesforce | CRM with AI features |
| DDOG | Datadog | Observability first; AI add-ons |
| DELL | Dell Technologies | General IT hardware |
| ANET | Arista Networks | Datacenter networking |
| EQIX | Equinix | Datacenter real estate |

---

## Out of scope — private AI outliers

Curated list of major **private** AI companies. **No public ticker → not in dataset.** Name them in notebook **limitations**; they explain what this study cannot price.

| Company | Segment | Note |
|---------|---------|------|
| OpenAI | Foundation models | ChatGPT / GPT; MSFT partner |
| Anthropic | Foundation models | Claude |
| xAI | Foundation models | Grok |
| Cohere | Foundation models | Enterprise LLMs |
| Mistral AI | Foundation models | European lab |
| AI21 Labs | Foundation models | Enterprise NLP |
| Stability AI | Foundation models | Stable Diffusion |
| Databricks | Data & AI platform | Large private data/AI stack |
| Scale AI | AI infrastructure | Training data / labeling |
| Hugging Face | AI infrastructure | Model hub & tools |
| Together AI | AI infrastructure | Model hosting |
| Anysphere | AI applications | Cursor (code editor) |
| Perplexity | AI applications | AI search |
| Character.ai | AI applications | AI chat |
| Midjourney | AI applications | Image generation |
| Runway | AI applications | Video AI |
| ElevenLabs | AI applications | Voice AI |
| Cognition | AI applications | Devin (coding agent) |
| Harvey | AI applications | Legal AI |
| Glean | AI applications | Enterprise search |
| Writer | AI applications | Enterprise gen AI |
| Figure AI | Robotics | Humanoid robots |
| 1X Technologies | Robotics | Humanoid robots |
| Skild AI | Robotics | Robotics foundation models |
| Anduril | Defense AI | Autonomous defense systems |
| Shield AI | Defense AI | Autonomous aircraft |

**Also out of scope (not in either list):** extra public tickers beyond MSFT and GOOGL; auto/robotics **public** names (e.g. TSLA) where AI is not the core revenue story.

**Limitations line for notebook:**

> Major AI innovation sits in private companies (OpenAI, Anthropic, Databricks, Cursor, etc.) with no public financials. This EDA compares **two listed AI-exposed megacaps** (Microsoft and Alphabet) — not chipmakers, the full hyperscaler group, private AI labs, or the full AI economy.

---

## Data sources

| Priority | Source | Link | Use |
|----------|--------|------|-----|
| 1 | **yfinance** | [pypi.org/project/yfinance](https://pypi.org/project/yfinance/) | Primary fetch — phase B |
| 2 | SEC EDGAR | [sec.gov/edgar](https://www.sec.gov/edgar) | Verify US filings if needed |
| 3 | FMP / Alpha Vantage | [financialmodelingprep.com](https://site.financialmodelingprep.com/) · [alphavantage.co](https://www.alphavantage.co/) | Backup APIs (key required) |
| 4 | FRED | [fred.stlouisfed.org](https://fred.stlouisfed.org/) | Optional macro context (phase H) |

**Minimum fields per public company:** `symbol`, `company_name`, `category`, `fiscal_year_end`, reported P&L lines, current market cap, P/E, P/S, total revenue, margins, and price.

**Final analysis_data:** Use the Phase D source exports, `merged_financials.csv` and `merged_info.csv`, plus the Phase E joined notebook input, `analysis_base.csv`. This is a compact fundamentals comparison rather than a daily price-history project.

---

## Checklist

- [x] Research goal & ethics  
- [x] MSFT vs GOOGL public scope + exclusions + private outliers list  
- [x] Data sources  
- [x] Mentor approval  

**Phase A is complete.** Row-count verification and notebook copy of scope → [phase B](B-import-and-first-look.md).

## Deliverable (handed to phase B)

Copy research goal, two-company scope, private outliers, and limitations into [`notebooks/main.ipynb`](../notebooks/main.ipynb) intro (phase B deliverable).
