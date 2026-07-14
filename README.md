# Internship & Research – Morris de Lange

This repository collects research outputs from my MSc International Business & Management at the University of Groningen and my internship as **International Management Consultant** at [Resilience BV](https://resiliencebv.com) (Addis Ababa & Cape Town, Sept–Nov 2025), focused on private-sector development in agrologistics, seed-sector development, sustainable agriculture, and trade.

---

## 1. Master's Thesis — Strategic Responses to Populism and Corporate ESG Performance in Europe (2010–2024)

This empirical study investigates how the presence of right- and left-wing populist parties in national home-country governments shapes the Environmental, Social, and Governance (ESG) performance of publicly listed domestic firms and Multinational Enterprises (MNEs) across 23 European countries.

### Key Findings
* **Right-Wing Populism:** Exhibits a significant lagged negative effect ($\beta = -1.74$, $p < 0.01$) on aggregate corporate ESG scores, driven heavily by disruptions to the environmental and social pillars.
* **Left-Wing Populism:** Shows a direct, significant positive effect on environmental and social sustainability measures.
* **MNE Moderation:** International exposure significantly dampens the institutional pressures exerted by right-wing populist regimes, acting as a strategic safeguard.

### Quantitative Skills & Methodology
To isolate these mechanisms and overcome systemic data limitations, the quantitative analysis employs advanced econometric and data management techniques:

* **Panel Data Econometrics:** Implements **Fixed Effects (FE) panel regressions** to control for unobserved, time-invariant firm-level heterogeneity. Model selection was validated via a **Hausman specification test** ($p < 0.000$).
* **Temporal Dynamics (Lag Structures):** Accounts for delayed institutional effects by executing a three-year lag structure ($L=3$) for right-wing populism, backed by empirical lag validation tests.
* **Advanced Imputation:** Mitigated potential selection and survivorship bias arising from missing historical ESG data by developing an **industry-year mean single imputation** strategy, successfully expanding the sample while neutralizing artificial linearity.
* **Statistical Rigor:** Corrected for heteroscedasticity and within-firm serial correlation utilizing **Variance-Covariance Error (VCE) estimators with standard errors clustered at the firm level**. Addressed multicollinearity through Variance Inflation Factor (VIF) diagnostics (Mean VIF = 2.48).
* **Robustness & Boundary Conditions:** Validated findings using subsample cross-examinations, splitting the data across:
  * *Exogenous Regime Shifts:* Pre- and Post-Paris Climate Agreement (2015) operational windows.
  * *Performance Stratification:* "ESG Leaders Only" sample splits (scores $\geq$ 75).
  * *Sectoral Materialities:* High ESG-sensitivity industry subsets (Energy, Materials, Biotech).

`Master_Thesis_Morris_de_Lange.pdf` — the full-text academic report detailing the theoretical framework (Stakeholder and Institutional theories), variables, and extended discussion.

---

## 2. Replication Code

The statistical analysis behind the thesis, provided in two versions:

* `europe_esg_analysis.do`: The comprehensive **Stata** batch file containing code for single data imputation, data merging (Refinitiv, Timbro, ThePopuList, Orbis, and World Bank databases), fixed effects panel estimations, cross-lag checking, and descriptive statistics.
* `europe_esg_analysis.py`: A **Python** translation of the same pipeline using `pandas`, `statsmodels`, and `linearmodels` (`PanelOLS`), with notes on approximating Stata's `xtabond2` System-GMM via `pydynpd`.

> **Note:** The scripts reference proprietary source data (LSEG Refinitiv, Bureau van Dijk Orbis, Timbro) that is not included in this repository. The `BASE_DIR` / file paths at the top of each script must be adjusted to your own environment.

### Tech Stack & Data Sources
* **Software:** Stata & Python (data structuring, long-format panel generation, regression modeling)
* **Firm-Level Data:** LSEG Refinitiv (ESG metrics), Bureau van Dijk Orbis (financial controls & foreign sales ratios)
* **Political & Macro Data:** Timbro Dataset, ThePopuList, World Bank Development Indicators

---

## 3. Internship Report — Bottlenecks Affecting the Competitiveness and Sustainability of Ethiopian Horticultural Exports

A report developed by **Resilience BV** for the EU-funded **MAHEBER programme** (implemented by COLEAD), to which I contributed as co-author during my internship.

### Overview
The study diagnoses the main structural and cyclical bottlenecks constraining Ethiopian horticultural exports and proposes pragmatic, evidence-based recommendations for public and private decision-makers. It adopts an export-oriented, value-chain approach spanning input supply, production, aggregation, post-harvest handling, logistics, standards compliance, and market development.

### Methodology
* **Mixed-methods design:** A quantitative dataset (2009–2023 production, area, yield, and trade data), **37 semi-structured stakeholder interviews**, and a structured survey.
* **Prioritisation:** Bottlenecks were validated and scored in an expert workshop (25+ participants) and classified into **Tier 1 / Tier 2** based on impact and actionability.
* **Benchmarking:** Ethiopia's export performance assessed against regional competitors, notably **Kenya and Egypt**.

### Central Finding
Ethiopia's core challenge is not a lack of agro-ecological potential but a systemic **"export system maturity" gap**: floriculture demonstrates a mature, reliable export system, while fruits and vegetables remain at an earlier stage marked by fragmented production, weak aggregation and cold chain, limited quality infrastructure, and reactive market engagement.

`Bottlenecks Affecting the Competitiveness and Sustainability of Ethiopian Horticultural Exports.pdf`

---

## Author
**Morris de Lange** — MSc International Business & Management, University of Groningen
[LinkedIn](https://www.linkedin.com/in/morrisdelange/)

## Note on Use
The MAHEBER report is the intellectual property of COLEAD and is shared here for reference and portfolio purposes; its content is the sole responsibility of COLEAD and does not necessarily reflect the official position of the European Union. The thesis and replication code are shared for academic and portfolio purposes.
