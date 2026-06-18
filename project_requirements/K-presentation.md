# K — Presentation

**EDA guide:** Presentation guide (8–12 minutes)  
**When:** After notebook and dashboard are ready

---

## Goal

Tell the story orally: question → data → evidence → cautious conclusion.

## Required topics (cover all eight)

| # | Topic | What to say |
|---|--------|-------------|
| 1 | **Goal** | What question are you answering? |
| 2 | **Topic** | Why compare Microsoft and Google on AI valuation? |
| 3 | **Data source** | yfinance, filings proxy, limitations, trust |
| 4 | **Highlights** | 2–4 best Streamlit dashboard views (not every plot) |
| 5 | **Surprise** | One unexpected finding |
| 6 | **Usefulness** | Who could use this? (analysts, students, general audience) |
| 7 | **Difficulties** | Missing data, row count, API limits, time |
| 8 | **Conclusions** | Hypothesis + what you’d do next |

## Suggested slide flow (~10 slides)

1. Title + one-sentence question  
2. Why this topic matters  
3. Data sources & two-company scope  
4. Methods (metrics: revenue, margin, P/S, P/E — one diagram)  
5. Finding 1 (chart)  
6. Finding 2 (chart)  
7. Finding 3 (chart or table)  
8. Surprise / limitation  
9. Hypothesis: MSFT or GOOGL looks more reasonable?  
10. Next steps + thank you  

## Practice tips

- Stay within **8–12 minutes**
- Explain charts without reading code
- End with **limitations** and “not investment advice”
- Keep the Streamlit dashboard demo to **≤ 2 minutes**

## Deliverable

Slides: [`PRESENTATION.md`](../PRESENTATION.md) (Marp markdown, ~8 cue-card slides) + practiced talk.

Export to PDF/PPTX with [Marp CLI](https://github.com/marp-team/marp-cli) if needed:  
`marp PRESENTATION.md --pdf` or `marp PRESENTATION.md --pptx`

## Done

Return to [`README.md`](../README.md) before submit. Dashboard demo: [`app/app.py`](../app/app.py).
