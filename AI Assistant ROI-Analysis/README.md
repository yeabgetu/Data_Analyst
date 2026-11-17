# AI assistant ROI: a sample analysis of real chatbot conversations

**Question:** How much time does an AI assistant actually save, and where does it fail?

## Key findings
- **Only 59% of conversations delivered business value.** About a third were chit-chat, role-play, or other non-work use.
- **The most common task fails most often.** Factual questions made up 28% of conversations and failed 22% of the time, often from invented facts.
- **6.7 minutes saved per conversation** (95% CI 5.8–7.7), about **112 hours per 1,000 conversations**.
- **The result holds under every assumption:** 3.3 minutes saved in the pessimistic scenario, 9.4 in the optimistic one.

## Data
193 English, non-toxic conversations sampled from the public [WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) dataset. 5 conversations were excluded for sexual or fetish content that passed the dataset's toxicity filter. Raw conversations are not published; only labels and aggregated results.

## Method
1. Labeled each conversation by task type and outcome (useful / partial / failed). Rules are in `codebook.md`. Labels were AI-assisted with human review.
2. Applied time-saved assumptions per task type under low, base, and high scenarios, counting full savings for useful outcomes, half for partial, and none for failed.
3. Estimated a 95% confidence interval with 5,000 bootstrap resamples.

## Limitations
- Time savings are assumptions, not measurements.
- The confidence interval reflects sampling uncertainty only; the scenarios reflect assumption uncertainty.
- Categories with fewer than 10 conversations are too small to compare reliably.

## How to make this production-grade
- Measure real baseline task times with users.
- Run a with-AI vs. without-AI pilot.
- Track whether outputs were actually used, not just generated.

## Files
- `report.pdf`: one-page report
- `analysis.ipynb`: sampling and analysis code
- `codebook.md`: labeling rules and time assumptions
- `labels_only.csv`: category and outcome per conversation id
- `kpis.csv`, `by_category.csv`: aggregated results

## Reproduce
```
uv sync
```
Then run `analysis.ipynb`.

## Made by
Yeab Getu · [LinkedIn](https://linkedin.com/in/yeab-getu-963394214)
