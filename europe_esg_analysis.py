"""
Europe ESG & Populism thesis analysis
Vertaling van Stata-code naar Python.

Vereiste packages:
    pip install pandas numpy openpyxl statsmodels linearmodels pydynpd

Opmerkingen bij de vertaling:
- Stata's `xtset` / `xtreg, fe` -> linearmodels PanelOLS met entity/time effects.
- Stata's `xtabond2` (system-GMM) heeft geen 1-op-1 equivalent in Python.
  De `pydynpd` package benadert Arellano-Bond / Blundell-Bond system-GMM het best.
  Onderaan staat een voorbeeld; verwacht kleine numerieke verschillen t.o.v. Stata.
- Pas BASE_DIR aan naar je eigen map.
"""

import os
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# 0. Instellingen
# ---------------------------------------------------------------------------
BASE_DIR = "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only"


def path(name):
    return os.path.join(BASE_DIR, name)


# ---------------------------------------------------------------------------
# 1. ESG-data van alle landen inladen en samenvoegen (import excel + append)
# ---------------------------------------------------------------------------
countries = [
    "Hungary", "Italy", "France", "Greece", "Poland", "CzechRepublic",
    "Romania", "Netherlands", "Cyprus", "Slovakia", "Slovenia", "Latvia",
    "Switzerland", "Ireland", "Sweden", "Spain", "Belgium", "Finland",
    "Denmark", "Austria", "Iceland", "Lithuania", "Bulgaria", "Germany",
    "Estonia", "Norway", "Croatia", "Luxembourg", "Portugal",
    "UnitedKingdom", "Malta",
]

frames = []
for c in countries:
    df = pd.read_excel(path(f"{c}_AllPublic.xlsx"), sheet_name="Sheet1")
    frames.append(df)

europe = pd.concat(frames, ignore_index=True)

# Slovak Republic -> Slovakia (zoals in de Stata-code na de Slovakia append)
europe["CountryofHeadquarters"] = europe["CountryofHeadquarters"].replace(
    "Slovak Republic", "Slovakia"
)

europe.to_pickle(path("EuropeDataset.pkl"))


# ---------------------------------------------------------------------------
# 2. Reshape long: ESG-scores van wide naar long (reshape long ... j(year))
# ---------------------------------------------------------------------------
# In Stata: variabelen als ESGscore2010, ESGscore2011, ... worden gestapeld
# tot ESGscore met een aparte year-kolom, met IdentifierRIC als id.
stub_vars = [
    "ESGscore",
    "EnvironmentalPillarScore",
    "SocialPillarScore",
    "GovernancePillarScore",
]


def reshape_long(df, stubs, i, j="year"):
    """Equivalent van Stata's `reshape long stub*, i(i) j(year)`."""
    long_df = pd.wide_to_long(
        df, stubnames=stubs, i=i, j=j
    ).reset_index()
    return long_df


europe = reshape_long(europe, stub_vars, i="IdentifierRIC")
europe.to_pickle(path("EuropeDataset.pkl"))


# ---------------------------------------------------------------------------
# 3. Populisme-data inladen (uit API-2024.xlsx) en reshapen
# ---------------------------------------------------------------------------
def load_and_reshape_populism(sheet, stub, i="country", j="year", rename_to=None):
    df = pd.read_excel(path("API-2024.xlsx"), sheet_name=sheet)
    long_df = pd.wide_to_long(df, stubnames=stub, i=i, j=j).reset_index()
    if rename_to:
        long_df = long_df.rename(columns={stub: rename_to})
    return long_df


populism_score = load_and_reshape_populism("Populism vote share", "populism_")
popgov = load_and_reshape_populism(
    "Populists in government all", "popgov_", rename_to="popgov_dummy"
)
popright = load_and_reshape_populism(
    "Right-Populists in government", "popright_", rename_to="popright_dummy"
)
popleft = load_and_reshape_populism(
    "Left-Populists in government", "popleft_", rename_to="popleft_dummy"
)
poptype = load_and_reshape_populism("Variety of populism", "poptype_")
# poptype labels: -1 = Left-populist, 0 = Other, 1 = Right-populist
# (in pandas als categorie of gewoon numeriek laten; hier numeriek gelaten)

farright = load_and_reshape_populism("Radical Right", "farright_")
farleft = load_and_reshape_populism("Radical left", "farleft_")


# ---------------------------------------------------------------------------
# 4. Alle populisme-datasets mergen (1:1 op country year)
# ---------------------------------------------------------------------------
populism_full = populism_score
for other in [farright, farleft, popgov, popright, popleft, poptype]:
    populism_full = populism_full.merge(other, on=["country", "year"], how="outer")

populism_full.to_pickle(path("API-2024_full_populism.pkl"))


# ---------------------------------------------------------------------------
# 5. Populisme aan de ESG-dataset koppelen (merge m:1 country year)
# ---------------------------------------------------------------------------
europe = europe.rename(columns={"CountryofHeadquarters": "country"})
europe = europe.merge(populism_full, on=["country", "year"], how="left")

if "CountryofExchange" in europe.columns:
    europe = europe.drop(columns=["CountryofExchange"])


# ---------------------------------------------------------------------------
# 6. Industry & country encoderen; missende ESG-scores droppen
# ---------------------------------------------------------------------------
europe = europe.rename(columns={"GICSIndustryGroupName": "industry"})
europe["industry_id"] = pd.Categorical(europe["industry"]).codes + 1
europe["country_id"] = pd.Categorical(europe["country"]).codes + 1

europe = europe.dropna(subset=["ESGscore"])
europe.to_pickle(path("EuropeDataset.pkl"))


# ---------------------------------------------------------------------------
# 7. Missende ISIN-codes toevoegen
# ---------------------------------------------------------------------------
isin_missing = pd.read_excel(path("ISIN_missing.xlsx"), sheet_name="Sheet1")
# Verondersteld: kolom met vervangende code heet ISINCode2
europe = europe.merge(
    isin_missing[["IdentifierRIC", "year", "ISINCode2"]],
    on=["IdentifierRIC", "year"],
    how="left",
)
mask = europe["ISINCode"].isna() & europe["ISINCode2"].notna()
europe.loc[mask, "ISINCode"] = europe.loc[mask, "ISINCode2"]
europe = europe.drop(columns=["ISINCode2"])


# ---------------------------------------------------------------------------
# 8. Firm-specifieke control variables toevoegen via ISINCode (reshape long + merge)
# ---------------------------------------------------------------------------
cv_stubs = [
    "OperatingRevenue_", "PLbeforetax_", "TotalAssets_",
    "ProfitMargin_", "ROE_", "SolvencyRatio_",
]
cv = pd.read_excel(path("Firm-specific CVs.xlsx"), sheet_name="Results")
cv_long = pd.wide_to_long(cv, stubnames=cv_stubs, i="ISINCode", j="year").reset_index()

europe = europe.merge(cv_long, on=["ISINCode", "year"], how="left")

# destring ... , force  ->  to_numeric met errors="coerce"
for col in ["ProfitMargin_", "ROE_", "SolvencyRatio_"]:
    europe[col] = pd.to_numeric(europe[col], errors="coerce")

europe["log_OperatingRevenue"] = np.log(europe["OperatingRevenue_"])
europe["log_TotalAssets"] = np.log(europe["TotalAssets_"])


# ---------------------------------------------------------------------------
# 9. Macro-controls toevoegen
# ---------------------------------------------------------------------------
macro = pd.read_excel(path("Macro controls.xlsx"), sheet_name="Data")

# In Stata worden kolommen C..Q hernoemd naar year2010..year2024, daarna
# dubbel gereshaped naar long en weer wide per macro_control_name.
# In pandas doen we dat via melt + pivot.
year_cols = [c for c in macro.columns if str(c).startswith("year")]
# Als de jaarkolommen nog niet die naam hebben, hernoem hier eventueel handmatig.

macro = macro.dropna(subset=["macro_control_name"])

macro_long = macro.melt(
    id_vars=["country", "macro_control_name"],
    value_vars=year_cols,
    var_name="year",
    value_name="value",
)
macro_long["year"] = macro_long["year"].str.replace("year", "").astype(int)

# Terug naar wide: iedere macro_control_name wordt een eigen kolom
macro_wide = macro_long.pivot_table(
    index=["country", "year"], columns="macro_control_name", values="value"
).reset_index()

macro_wide["country"] = macro_wide["country"].replace(
    {"Slovak Republic": "Slovakia", "Czechia": "Czech Republic"}
)

europe = europe.merge(macro_wide, on=["country", "year"], how="left")

if "Interest" in europe.columns:
    europe = europe.drop(columns=["Interest"])

# Opnieuw cleanen
europe = europe.dropna(subset=["ESGscore"])
europe.to_pickle(path("EuropeDataset.pkl"))


# ---------------------------------------------------------------------------
# 10. Paneldata instellen (xtset)
# ---------------------------------------------------------------------------
# duplicates drop IdentifierRIC year, force
europe = europe.drop_duplicates(subset=["IdentifierRIC", "year"], keep="first")

europe["IdentifierRIC_id"] = pd.Categorical(europe["IdentifierRIC"]).codes + 1

# Panelstructuur: sorteer op id + jaar, gebruik MultiIndex voor lags
europe = europe.sort_values(["IdentifierRIC_id", "year"]).reset_index(drop=True)


def add_lag(df, var, group="IdentifierRIC_id"):
    """L.var equivalent: 1-periode lag binnen dezelfde firm."""
    return df.groupby(group)[var].shift(1)


# Change-in-ESG variabelen (gen change = X - L.X)
for base in ["ESGscore", "EnvironmentalPillarScore",
             "SocialPillarScore", "GovernancePillarScore"]:
    lag = add_lag(europe, base)
    change_name = "change_" + base.replace("PillarScore", "")
    # change_ESGscore, change_Environmental, change_Social, change_Governance
    if base == "ESGscore":
        change_name = "change_ESGscore"
    europe[change_name] = europe[base] - lag

# Gemiddelde ESG-score per industry per year (egen mean, by industry year)
europe["mean_ESG_industry"] = europe.groupby(
    ["industry_id", "year"]
)["ESGscore"].transform("mean")

europe.to_pickle(path("EuropeDataset.pkl"))


# ---------------------------------------------------------------------------
# 11. DESCRIPTIVES
# ---------------------------------------------------------------------------
desc_vars = [
    "ESGscore", "EnvironmentalPillarScore", "SocialPillarScore",
    "GovernancePillarScore", "popgov_dummy", "popright_dummy", "popleft_dummy",
]

print("\n=== Summary statistics ===")
print(europe[desc_vars].describe().T)

# Correlatiematrix (pwcorr). p-waarden erbij via losse berekening.
from scipy import stats


def corr_with_pvalues(df, cols):
    sub = df[cols].dropna()
    corr = sub.corr()
    pvals = pd.DataFrame(np.ones_like(corr), columns=cols, index=cols)
    for a in cols:
        for b in cols:
            if a != b:
                r, p = stats.pearsonr(sub[a], sub[b])
                pvals.loc[a, b] = p
    return corr, pvals


print("\n=== Correlation matrix ===")
corr, pvals = corr_with_pvalues(europe, desc_vars)
print(corr.round(3))
print("\n=== P-values ===")
print(pvals.round(3))


# ---------------------------------------------------------------------------
# 12. Regressies
# ---------------------------------------------------------------------------
import statsmodels.formula.api as smf
from linearmodels.panel import PanelOLS

# --- Simpele OLS met year-dummies (reg ESGscore i.year) ---
ols_model = smf.ols("ESGscore ~ C(year)", data=europe).fit(
    cov_type="HC1"
)
print("\n=== OLS: ESGscore ~ i.year ===")
print(ols_model.summary())

# --- Fixed-effects panel (xtreg ESGscore ..., fe) ---
panel = europe.set_index(["IdentifierRIC_id", "year"])
fe_model = PanelOLS.from_formula(
    "ESGscore ~ popright_dummy + popleft_dummy + EntityEffects + TimeEffects",
    data=panel,
).fit(cov_type="clustered", cluster_entity=True)
print("\n=== Fixed effects: ESGscore popright popleft i.year ===")
print(fe_model)


# ---------------------------------------------------------------------------
# 13. System-GMM (xtabond2) -- benadering via pydynpd
# ---------------------------------------------------------------------------
# xtabond2 heeft geen exact Python-equivalent. pydynpd is de dichtstbijzijnde.
# Voorbeeld (uncomment en pas de kolomnamen aan zodra pydynpd geïnstalleerd is):
#
# from pydynpd import regression
#
# gmm_data = europe.dropna(subset=[
#     "ESGscore", "popright_dummy", "popleft_dummy",
#     "log_OperatingRevenue", "log_TotalAssets"
# ]).copy()
#
# command = (
#     "ESGscore L.ESGscore popright_dummy popleft_dummy "
#     "log_OperatingRevenue log_TotalAssets | "
#     "gmm(ESGscore, 1:5) iv(log_OperatingRevenue log_TotalAssets) | "
#     "timedumm twostep"
# )
# gmm = regression.abond(command, gmm_data, ["IdentifierRIC_id", "year"])
#
# Let op: syntax en identificatie van instrumenten wijken af van Stata;
# controleer de resultaten en de Hansen/AR(2)-tests handmatig.

print("\nKlaar. Dataset opgeslagen als EuropeDataset.pkl")
