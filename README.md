# Strategic Responses to Populism and Corporate ESG Performance in Europe (2010-2024)

This repository contains the replication code and documentation for my Master's Thesis in MSc International Business & Management at the University of Groningen. 

## Project Overview
This empirical study investigates how the presence of right- and left-wing populist parties in national home-country governments shapes the Environmental, Social, and Governance (ESG) performance of publicly listed domestic firms and Multinational Enterprises (MNEs) across 23 European countries. 

### Key Findings
* **Right-Wing Populism:** Exhibits a significant lagged negative effect ($\beta = -1.74$, $p < 0.01$) on aggregate corporate ESG scores, driven heavily by disruptions to the environmental and social pillars.
* **Left-Wing Populism:** Shows a direct, significant positive effect on environmental and social sustainability measures.
* **MNE Moderation:** International exposure significantly dampens the institutional pressures exerted by right-wing populist regimes, acting as a strategic safeguard.

---

## Quantitative Skills & Methodology
To isolate these mechanisms and overcome systemic data limitations, the quantitative analysis employs advanced econometric and data management techniques:

* **Panel Data Econometrics:** Implements **Fixed Effects (FE) panel regressions** to control for unobserved, time-invariant firm-level heterogeneity. Model selection was validated via a **Hausman specification test** ($p < 0.000$).
* **Temporal Dynamics (Lag Structures):** Accounts for delayed institutional effects by executing a three-year lag structure ($L=3$) for right-wing populism, backed by empirical lag validation tests.
* **Advanced Imputation:** Mitigated potential selection and survivorship bias arising from missing historical ESG data by developing an **industry-year mean single imputation** strategy, successfully expanding the sample while neutralizing artificial linearity.
* **Statistical Rigor:** Corrected for heteroscedasticity and within-firm serial correlation utilizing **Variance-Covariance Error (VCE) estimators with standard errors clustered at the firm level**. Addressed multicollinearity through Variance Inflation Factor (VIF) diagnostics (Mean VIF = 2.48).
* **Robustness & Boundary Conditions:** Validated findings using subsample cross-examinations, splitting the data across:
  * *Exogenous Regime Shifts:* Pre- and Post-Paris Climate Agreement (2015) operational windows.
  * *Performance Stratification:* "ESG Leaders Only" sample splits (scores $\geq$ 75).
  * *Sectoral Materialities:* High ESG-sensitivity industry subsets (Energy, Materials, Biotech).

---

## Repository Structure
* `Official dataset [Europe only] 2.do`: The comprehensive Stata batch file containing code for single data imputation, data merging (Refinitiv, Timbro, ThePopuList, Orbis, and World Bank databases), fixed effects panel estimations, cross-lag checking, and descriptive statistics.
* `Master_Thesis_Morris_de_Lange.pdf`: The full-text academic report detailing the theoretical framework (Stakeholder and Institutional theories), variables, and extended discussion.

---

## Tech Stack & Data Sources
* **Software:** Stata (Data structuring, long-format panel generation, regression modeling)
* **Firm-Level Data:** LSEG Refinitiv (ESG metrics), Bureau van Dijk Orbis (Financial controls & foreign sales ratios)
* **Political & Macro Data:** Timbro Dataset, ThePopuList, World Bank Development Indicators
