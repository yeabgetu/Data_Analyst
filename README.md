# Yeab Getu — Data Analyst

Economics graduate turning business data into decisions. I combine SQL, Python and Power BI with econometrics training from my degree to build dashboards, investigate business problems, test hypotheses and quantify opportunities. My work spans financial services, commodity markets, AI productivity, pricing intelligence and e-commerce analytics.

**Core:** SQL (PostgreSQL · BigQuery · CTEs · Window Functions) · Python (pandas · statsmodels · scipy · matplotlib) · Power BI (Data Modeling · DAX)

**Analytics:** A/B Testing · Hypothesis Testing · Time-Series Forecasting · Regression Analysis · Funnel Analysis · Statistical Inference · Scenario Analysis

**Also use:** Excel · Tableau · Stata · SPSS · Git · Google Colab

---

## Projects

### 🌍 Cross-Border Payment Cost Analysis: Banks vs. Non-Bank Providers

**SQL · Python · Data Analysis · Financial Services**

**Question:** How do banks compare with non-bank providers on the cost and speed of cross-border payments from South Africa?

- Analyzed World Bank Remittance Prices Worldwide data for six payment corridors in Q3 2025.
- **Banks cost 10–16% of the amount sent**, compared with 7–9% for non-bank providers, creating a cost gap of 2.5–7.1 percentage points.
- **No bank service settled within one hour** in any of the six corridors, while 33–75% of non-bank services offered settlement within an hour.
- Identified China (15.5%) and India (13.5%) as the most expensive bank payment corridors.
- Estimated that a business sending $10,000 monthly could save approximately $4,900–$7,400 annually per corridor by switching to a provider that is 40% cheaper.

**Use case:** Helps businesses evaluate international payment providers, identify expensive payment corridors and quantify potential savings.

→ [View cost comparison chart](https://github.com/yeabgetu/Data_Analyst/raw/main/corridor-cost-benchmark/corridor_costs.png)

### 🤖 AI Assistant ROI: Measuring Productivity and Failure Rates

**Python · Data Analysis · Statistical Analysis · Bootstrap**

**Question:** How much time does an AI assistant actually save, and where does it fail?

- Analyzed 193 English-language conversations from the public WildChat-1M dataset.
- Classified conversations by task type and outcome (useful, partial or failed), using AI-assisted labeling with human review.
- **Only 59% of conversations delivered business value**, while approximately one-third involved chit-chat, role-play or other non-work activities.
- Identified factual questions as the most common task (28% of conversations), with a 22% failure rate, often involving invented facts.
- Estimated **6.7 minutes saved per conversation**, with a 95% bootstrap confidence interval of 5.8–7.7 minutes.
- Estimated approximately 112 hours saved per 1,000 conversations.
- Tested pessimistic, base and optimistic assumptions, producing estimated savings of 3.3, 6.7 and 9.4 minutes respectively.

**Methodology:** 5,000 bootstrap resamples for confidence interval estimation, with separate scenario analysis to account for uncertainty in time-saving assumptions.

**Use case:** Helps organizations assess AI assistant productivity, identify high-failure task categories and determine where human verification or workflow improvements are necessary.

→ [View AI ROI dashboard](https://private-user-images.githubusercontent.com/222705993/708868233-8da07f1e-7e36-4122-9245-632bd69c9508.png)

### ☕ Coffee Price Risk: What the Arabica Boom Means for Ethiopia

**Python · pandas · statsmodels · matplotlib · uv**

**Question:** How risky are today's coffee prices, and what could price swings mean for Ethiopia's coffee export revenue?

- Cleaned 66 years of World Bank monthly prices (1960–2026, 802 months) into a tidy Arabica and Robusta series.
- Arabica costs 2.04x Robusta, above its post-1990 average of 1.82x and higher than 69% of months since 1990; the premium nearly vanished in 2024 (≈1.2x).
- Identified two market eras: a stable premium under the coffee quota system until 1989, volatile since, which makes the 66-year average misleading.
- Recent volatility (7.3% typical monthly swing) is only slightly above the post-1990 norm (6.6%): high prices, not chaos.
- An ARIMA model did not beat a "no change" forecast in a 12-month backtest (19.0% vs. 17.8% error), so I reported an 80% range ($4.97–$11.02/kg by October 2027) instead of a single forecast.
- Translated that range into Ethiopia's export revenue: about $2.0–4.5 billion per year, versus about $3.0 billion today.

**Use case:** Helps exporters, banks and policymakers assess coffee price exposure and understand the potential impact of global commodity market movements on Ethiopia's foreign-currency earnings.

→ [View project](https://github.com/yeabgetu/Data_Analyst/tree/main/ethiopia-coffee-premium)

### ☕ Coffee Quality & Pricing Intelligence

**Python · pandas · statsmodels · Regression**

**Question:** What drives coffee price, and which high-quality lots look underpriced?

- Cleaned 35,700 records down to 35,000 unique lots (deduplication, revision handling, country-level imputation).
- **Quality alone explains only ~11% of price** (r = 0.34). Buyer segment matters more: specialty lots average $9.97/kg vs. $3.88 for commodity, with only a 4-point quality gap.
- Built a pricing benchmark from quality, origin, processing, certification and buyer segment (R² = 0.79).
- **Flagged 2,578 high-quality lots (29%) priced ≥10% below benchmark.** Kenya (33%) and Ethiopia (31%) had the highest opportunity rates.
- Developed a quality model (R² = 0.85) with VIF checks and HC3 robust errors after a Breusch-Pagan test.

**Use case:** A pricing intelligence and screening tool for coffee buyers to prioritize sourcing opportunities and support negotiation decisions.

→ [View project](https://github.com/yeabgetu/Data_Analyst/blob/main/Coffee%20Quality%20And%20Pricing%20Analysis)

### 🛒 E-Commerce Product Analysis

**PostgreSQL · Python · Power BI**

**Question:** Where is the store losing revenue between visit and purchase?

- Analyzed 25,000 sessions, 3,037 orders and 400 SKUs with SQL (CTEs, window functions, conditional aggregation).
- **64% cart abandonment:** 5,455 of 8,492 carts never converted.
- **Mobile converts 2.4 percentage points lower than desktop** (11.0% vs. 13.4%) and abandons more.
- Paid Search drove the most revenue; Organic brought the most traffic but converted worst (11.6%).
- Built an interactive Power BI dashboard covering KPIs, channels, devices and monthly trends.

**Use case:** Identifies checkout friction and mobile UX as potential revenue improvement opportunities.

→ [View project](https://github.com/yeabgetu/Data_Analyst/blob/main/Ecommerce%20Product%20Analysis) · [View dashboard](https://private-user-images.githubusercontent.com/222705993/682709962-d9c556ba-ee2c-4127-ad7d-35c3f0a7c79d.png)

### 📊 E-Commerce A/B Test & Revenue Forecast

**BigQuery · BigQuery ML · Python · Power BI**

**Question:** Is mobile checkout really converting worse than desktop, and what is it worth?

- Migrated 25,000 sessions and 3,037 orders from PostgreSQL to BigQuery and validated the move (0 duplicates, 0 cross-table mismatches).
- **Mobile checkout converts 2.9 percentage points lower** (34.3% vs. 37.2% of carts, p ≈ 0.005, 95% CI −5.0 to −0.9), tested with a two-proportion z-test after a power analysis.
- **Not a traffic-mix effect:** the gap is unchanged after adjusting for channel (Cochran–Mantel–Haenszel) and is concentrated in Paid Social (−8.1 points).
- Estimated the checkout gap costs about $7,800/year; mobile's lower add-to-cart rate is a bigger lever (about $20,300/year).
- Forecast Q1 2026 revenue at ~$16,300/month with BigQuery ML ARIMA_PLUS (backtest MAPE 2.9%).

**Use case:** Identifies mobile product pages and the Paid Social checkout journey as areas for investigation, with a randomized A/B test to validate proposed improvements.

→ [View project](https://github.com/yeabgetu/Data_Analyst/blob/main/Ecommerce-BigQuery-AB-Test-Forecas) · [View dashboard screenshot](https://private-user-images.githubusercontent.com/222705993/684840964-36aa64e3-6754-4bb4-a5ba-7ebe5518fe40.png)

---

## Approach

I focus on translating analytical work into practical business recommendations:

- **Understand:** Define the business question and identify the relevant metrics.
- **Analyze:** Collect, clean, validate and investigate data using SQL and Python.
- **Measure:** Apply statistical methods, forecasting and scenario analysis where appropriate.
- **Communicate:** Build dashboards and translate findings into actionable recommendations.

**Interested in:** Data Analyst · Business Analyst · Financial Services Analytics · Research Analyst · Business Intelligence opportunities.
