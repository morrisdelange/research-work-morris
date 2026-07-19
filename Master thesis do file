// DEZE DO FILE IS MET ESG SCORE GEMIDDELDE PER INDUSTRIE IPV ZE TE DROPPEN!!!

clear
cd "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only"

clear
import excel "Hungary_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Hungary_AllPublic.dta", replace
clear
import excel "Italy_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Italy_AllPublic.dta", replace
clear
import excel "France_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/France_AllPublic.dta", replace
clear
import excel "Greece_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Greece_AllPublic.dta", replace
clear
import excel "Poland_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Poland_AllPublic.dta", replace
clear
import excel "CzechRepublic_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/CzechRepublic_AllPublic.dta", replace
clear
import excel "Romania_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Romania_AllPublic.dta", replace
clear
import excel "Netherlands_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Netherlands_AllPublic.dta", replace
clear
import excel "Cyprus_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Cyprus_AllPublic.dta", replace
clear
import excel "Slovakia_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Slovakia_AllPublic.dta", replace
clear
import excel "Slovenia_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Slovenia_AllPublic.dta", replace
clear
import excel "Latvia_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Latvia_AllPublic.dta", replace
clear
import excel "Switzerland_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Switzerland_AllPublic.dta", replace
clear
import excel "Ireland_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Ireland_AllPublic.dta", replace
clear
import excel "Sweden_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Sweden_AllPublic.dta", replace
clear
import excel "Spain_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Spain_AllPublic.dta", replace
clear
import excel "Belgium_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Belgium_AllPublic.dta", replace
clear
import excel "Finland_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Finland_AllPublic.dta", replace
clear
import excel "Denmark_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Denmark_AllPublic.dta", replace
clear
import excel "Austria_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Austria_AllPublic.dta", replace
clear
import excel "Iceland_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Iceland_AllPublic.dta", replace
clear
import excel "Lithuania_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Lithuania_AllPublic.dta", replace
clear
import excel "Bulgaria_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Bulgaria_AllPublic.dta", replace
clear
import excel "Germany_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Germany_AllPublic.dta", replace
clear
import excel "Estonia_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Estonia_AllPublic.dta", replace
clear
import excel "Norway_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Norway_AllPublic.dta", replace
clear
import excel "Croatia_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Croatia_AllPublic.dta", replace
clear
import excel "Luxembourg_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Luxembourg_AllPublic.dta", replace
clear
import excel "Portugal_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Portugal_AllPublic.dta", replace
clear
import excel "UnitedKingdom_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/UnitedKingdom_AllPublic.dta", replace
clear
import excel "Malta_AllPublic.xlsx", sheet(Sheet1) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Malta_AllPublic.dta", replace

// ESG data van alle landen toevoegen aan dataset 
clear
use "Hungary_AllPublic.dta" 
append using "Italy_AllPublic.dta" 
append using "France_AllPublic.dta"
append using "Greece_AllPublic.dta"
append using "Poland_AllPublic.dta"
append using "CzechRepublic_AllPublic.dta"
append using "Romania_AllPublic.dta"
append using "Netherlands_AllPublic.dta"
append using "Cyprus_AllPublic.dta"
append using "Slovakia_AllPublic.dta"
replace CountryofHeadquarters = "Slovakia" if CountryofHeadquarters == "Slovak Republic"
append using "Slovenia_AllPublic.dta"
append using "Latvia_AllPublic.dta"
append using "Switzerland_AllPublic.dta"
append using "Ireland_AllPublic.dta"
append using "Sweden_AllPublic.dta"
append using "Spain_AllPublic.dta"
append using "Belgium_AllPublic.dta"
append using "Finland_AllPublic.dta"
append using "Denmark_AllPublic.dta"
append using "Austria_AllPublic.dta"
append using "Iceland_AllPublic.dta"
append using "Lithuania_AllPublic.dta"
append using "Bulgaria_AllPublic.dta"
append using "Germany_AllPublic.dta"
append using "Estonia_AllPublic.dta"
// Bij het inladen van Norway pakt ie soms de eerste rij niet. Dus aanpassen in Excel
append using "Norway_AllPublic.dta"
append using "Croatia_AllPublic.dta"
append using "Luxembourg_AllPublic.dta"
append using "Portugal_AllPublic.dta"
append using "UnitedKingdom_AllPublic.dta"
append using "Malta_AllPublic.dta"
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/EuropeDataset.dta", replace 

// We hoeven merge niet te gebruiken omdat alle vars hetzelfde zijn 
// Nu gaan we de reshape gebruiken 
clear
use "EuropeDataset.dta"
reshape long ESGscore EnvironmentalPillarScore SocialPillarScore GovernancePillarScore, i(IdentifierRIC) j(year)
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/EuropeDataset.dta", replace 

// Nu moeten we merge gebruiken om populisme toe te voegen aan de dataset 
// In de dataset staan alleen de election years, maar niet voor hoe lang!!!
clear
import excel "API-2024.xlsx", sheet(Populism vote share) firstrow
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/API-2024.dta", replace
reshape long populism_, i(country) j(year)
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/populism_score.dta", replace

// Dummy's toevoegen
clear
import excel "API-2024.xlsx", sheet(Populists in government all) firstrow
reshape long popgov_, i(country) j(year)
rename popgov_ popgov_dummy
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/popgov_dummy.dta", replace
clear
import excel "API-2024.xlsx", sheet(Right-Populists in government) firstrow
reshape long popright_, i(country) j(year)
rename popright_ popright_dummy
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/popright_dummy.dta", replace
clear
import excel "API-2024.xlsx", sheet(Left-Populists in government) firstrow
reshape long popleft_, i(country) j(year)
rename popleft_ popleft_dummy
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/popleft_dummy.dta", replace

// Dummy's toevoegen - Variety of populism
clear
import excel "API-2024.xlsx", sheet(Variety of populism) firstrow
reshape long poptype_, i(country) j(year)
label define poptype_lbl -1 "Left-populist" 0 "Other" 1 "Right-populist"
label values poptype_ poptype_lbl
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/poptype.dta", replace

// Radical right populism toevoegen aan de dataset (dit is nog fout, want ik moet ze allemaal tegelijk toevoegen)
clear
import excel "API-2024.xlsx", sheet(Radical Right) firstrow
reshape long farright_, i(country) j(year)
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/populism_farright.dta", replace 

// Radical left populism toevoegen aan de dataset 
clear
import excel "API-2024.xlsx", sheet(Radical left) firstrow
reshape long farleft_, i(country) j(year)
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/populism_farleft.dta", replace

// Merge populism_, populism_farleft, populism_farright, popgov_
clear
use "populism_score.dta"
merge 1:1 country year using "populism_farright.dta"
drop _merge
merge 1:1 country year using "populism_farleft.dta"
drop _merge
merge 1:1 country year using "popgov_dummy.dta"
drop _merge
merge 1:1 country year using "popright_dummy.dta"
drop _merge
merge 1:1 country year using "popleft_dummy.dta"
drop _merge
merge 1:1 country year using "poptype.dta"
drop _merge
save "API-2024_full_populism.dta", replace

clear
use "EuropeDataset.dta"
rename CountryofHeadquarters country
merge m:1 country year using "API-2024_full_populism.dta"
drop _merge CountryofExchange
save "EuropeDataset.dta", replace 

//rename industry
clear
use "EuropeDataset.dta", replace
rename GICSIndustryGroupName industry
encode industry, gen(industry_id)
encode country, gen(country_id)
save "EuropeDataset.dta", replace

// Missende ISINCodes toevoegen
clear
import excel "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/ISIN_missing.xlsx", sheet(Sheet1) firstrow 
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/ISIN_missing.dta", replace 
clear
use "EuropeDataset.dta"
merge 1:1 IdentifierRIC year using "ISIN_missing.dta", keepusing(ISINCode)
replace ISINCode = ISINCode2 if missing(ISINCode) & _merge == 3
drop ISINCode2
drop _merge
drop if missing(ISINCode)
save "EuropeDataset.dta", replace

// Moderation: Internationalization toevoegen
clear
import excel "Foreign Sales Ratio last available year.xlsx", firstrow
gen rowid = _n
sort rowid 

foreach var in ISINCode Revenue_millionsUSD CompanyName {
    gen `var'_filled = `var'
    replace `var'_filled = `var'_filled[_n-1] if missing(`var'_filled)
}

collapse (sum) SUB_Revenue_millionsUSD, by(ISINCode_filled CompanyName_filled Revenue_millionsUSD_filled)

capture confirm numeric variable Revenue_millionsUSD_filled
if _rc {
    destring Revenue_millionsUSD_filled, replace ignore(",")
}


gen Foreign_Sales_Ratio = SUB_Revenue_millionsUSD / Revenue_millionsUSD_filled

drop if Foreign_Sales_Ratio > 1

rename ISINCode_filled ISINCode
rename CompanyName_filled CompanyName
drop Revenue_millionsUSD_filled

replace Foreign_Sales_Ratio = 0 if Foreign_Sales_Ratio == .

duplicates drop ISINCode, force

* Maak dummy: is bedrijf een multinational? Rugman & Verbeke (2004)
gen MNC = Foreign_Sales_Ratio > 0.2
label define MNC_lbl 0 "Non-MNC" 1 "MNC"
label values MNC MNC_lbl

save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Foreign_Sales_Ratio.dta", replace

use "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/EuropeDataset.dta", clear
merge m:1 ISINCode using "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Foreign_Sales_Ratio.dta"
drop _merge
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/EuropeDataset.dta", replace


// Control variables toevoegen via ISINCode
clear
import excel "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Firm-specific CVs.xlsx", sheet(Results) firstrow
duplicates drop ISINCode, force
reshape long OperatingRevenue_ TotalAssets_ ROE_ SolvencyRatio_ ROA_ PLbeforetax_, i(ISINCode) j(year)
drop if missing(ISINCode)
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Firm-specific CVs long.dta", replace 

clear
use "EuropeDataset.dta"
merge m:1 ISINCode year using "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Firm-specific CVs long.dta"
drop _merge
destring ROE_, replace force
destring ROA_, replace force
destring SolvencyRatio_, replace force
gen log_OperatingRevenue = ln(OperatingRevenue)
gen log_TotalAssets = ln(TotalAssets)
save "EuropeDataset.dta", replace 


// Macro controls
clear 
import excel "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Macro controls.xlsx", sheet(Data) firstrow
rename (C D E F G H I J K L M N O P Q) (year2010 year2011 year2012 year2013 year2014 year2015 year2016 year2017 year2018 year2019 year2020 year2021 year2022 year2023 year2024)
drop if missing(macro_control_name)
reshape long year, i(country macro_control_name) j(time)
rename year value
rename time year
reshape wide value, i(country year) j(macro_control_name) string
rename value* *
replace country = "Slovakia" if country == "Slovak Republic"
replace country = "Czech Republic" if country == "Czechia"
save "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Macro controls.dta", replace

clear
use "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/EuropeDataset.dta"
merge m:1 country year using "/Users/morrisdelange_1/Documents/Stata/STATA thesis/Europe only/Macro controls.dta"
drop Interest
drop _merge
save "EuropeDataset.dta", replace 


// Paneldata instellen
clear
use "EuropeDataset.dta"
duplicates drop IdentifierRIC year, force
encode IdentifierRIC, gen(IdentifierRIC_id)
xtset IdentifierRIC_id year


// Industry average imputation
drop if missing(IdentifierRIC)
drop if missing(industry)
egen mean_ESG_industry = mean(ESGscore), by(industry_id year)
egen mean_EPillar_industry = mean(EnvironmentalPillarScore), by(industry_id year)
egen mean_SPillar_industry = mean(SocialPillarScore), by(industry_id year)
egen mean_GPillar_industry = mean(GovernancePillarScore), by(industry_id year)
replace ESGscore = mean_ESG_industry if missing(ESGscore)
replace EnvironmentalPillarScore = mean_EPillar_industry if missing(EnvironmentalPillarScore)
replace SocialPillarScore = mean_SPillar_industry if missing(SocialPillarScore)
replace GovernancePillarScore = mean_GPillar_industry if missing(GovernancePillarScore)
save "EuropeDataset.dta", replace 


// \/\/\/\/\/\/\/\/\/\/\/ \\ 
// DESCRIPTIVES
summarize ESGscore EnvironmentalPillarScore SocialPillarScore GovernancePillarScore popright_dummy popleft_dummy MNC log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment

// Correlation matrix
pwcorr ESGscore EnvironmentalPillarScore SocialPillarScore GovernancePillarScore popright_dummy popleft_dummy MNC log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, star(0.05)

// REGRESSIONS LINEAR
clear
use "EuropeDataset.dta"
reg ESGscore popright_dummy

// HAUSMANN
xtreg L.ESGscore popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
estimates store fe_model

xtreg L.ESGscore popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, re
estimates store re_model

hausman fe_model re_model // >> Komt FE uit


// REGRESSIONS PANEL DATA/ FIXED EFFECTS MODEL 1 2 3 4
clear 
use "EuropeDataset.dta"
gen interaction_popright = L3.popright_dummy * MNC
gen interaction_popleft = popleft_dummy * MNC
xtset IdentifierRIC_id year
* Model 1
xtreg ESGscore log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)

* Model 2
xtreg ESGscore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)

* Model 3
xtreg ESGscore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)

* Model 4
xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)

* Model 5
xtreg ESGscore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe 


* Model voorbeeld
clear 
use "EuropeDataset.dta"
gen interaction_popright = L3.popright_dummy * MNC
gen interaction_popleft = popleft_dummy * MNC
eststo clear
xtset IdentifierRIC_id year

eststo M1: xtreg ESGscore log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id) 
eststo M2: xtreg ESGscore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id) 
eststo M3: xtreg ESGscore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id) 
eststo M4: xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id) 
eststo M5: xtreg ESGscore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id) 

esttab M1 M2 M3 M4 M5 using regression_moderator.rtf, replace se b(%9.5f) star(* 0.1 ** 0.05 *** 0.01) label title("Regression Results – Moderation by Foreign Sales Ratio") mtitles("Model 1: Controls" "Model 2: IV1" "Model 3: IV2" "Model 4: IV1+2" "Model 5: Moderation") order(L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment) stats(r2 N N_g, fmt(3 0 0) labels("R-squared" "Observations" "Number of Firms")) 


// ROBUSTNESS CHECKS
* 1) Environmental, Social en Governance Score
clear
use "EuropeDataset.dta"

gen interaction_popright = L3.popright_dummy * MNC
gen interaction_popleft = popleft_dummy * MNC

xtset IdentifierRIC_id year

eststo clear

* Environmental
eststo E1: xtreg EnvironmentalPillarScore log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo E2: xtreg EnvironmentalPillarScore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo E3: xtreg EnvironmentalPillarScore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo E4: xtreg EnvironmentalPillarScore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo E5: xtreg EnvironmentalPillarScore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe

* Social
eststo S1: xtreg SocialPillarScore log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo S2: xtreg SocialPillarScore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo S3: xtreg SocialPillarScore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo S4: xtreg SocialPillarScore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo S5: xtreg SocialPillarScore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe

* Governance
eststo G1: xtreg GovernancePillarScore log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo G2: xtreg GovernancePillarScore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo G3: xtreg GovernancePillarScore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo G4: xtreg GovernancePillarScore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe
eststo G5: xtreg GovernancePillarScore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe

* Combineer alle modellen in één tabel
esttab E1 S1 G1 E2 S2 G2 E3 S3 G3 E4 S4 G4 E5 S5 G5 using ESG_pillars_15models.rtf, replace se b(%9.3f) star(* 0.1 ** 0.05 *** 0.01) label title("Regression Results – ESG Pillars per Model") mtitles("M1: Env" "M1: Soc" "M1: Gov" "M2: Env" "M2: Soc" "M2: Gov" "M3: Env" "M3: Soc" "M3: Gov" "M4: Env" "M4: Soc" "M4: Gov" "M5: Env" "M5: Soc" "M5: Gov") order(L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment) stats(r2 N N_g, fmt(3 0 0) labels("R-squared" "Observations" "Number of Firms"))


* 2) Alleen hoge bedrijven met Leader ESG scores
clear
use "EuropeDataset.dta"
gen interaction_popright = L3.popright_dummy * MNC
gen interaction_popleft = popleft_dummy * MNC
xtset IdentifierRIC_id year
eststo clear

eststo M1: xtreg ESGscore log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id)  
eststo M2: xtreg ESGscore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id) 
eststo M3: xtreg ESGscore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id) 
eststo M4: xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id) 
eststo M5: xtreg ESGscore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id) 

esttab M1 M2 M3 M4 M5 using regressionLeaderESG.rtf, replace b(%9.3f) se star(* 0.1 ** 0.05 *** 0.01)  title("Regression Results - Dependent Variable: ESG Score leaders only") mtitles("Model 1: Controls" "Model 2: IV1" "Model 3: IV2" "Model 4: IV1+2" "Model 5: Moderation") label order(L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment) stats(r2 N N_g, fmt(3 0 0) labels("R-squared" "Observations" "Number of Firms"))

* Start met een leeg document
xtreg ESGscore log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id)
outreg2 using regressionLeaderESG.doc, replace ctitle("Model 1: Controls") dec(3) label

* Append model 2
xtreg ESGscore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id)
outreg2 using regressionLeaderESG.doc, append ctitle("Model 2: IV1") dec(3) label

* Append model 3
xtreg ESGscore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id)
outreg2 using regressionLeaderESG.doc, append ctitle("Model 3: IV2") dec(3) label

* Append model 4
xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id)
outreg2 using regressionLeaderESG.doc, append ctitle("Model 4: IV1+2") dec(3) label

* Append model 5
xtreg ESGscore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if ESGscore >= 75, fe vce(cluster IdentifierRIC_id)
outreg2 using regressionLeaderESG.doc, append ctitle("Model 5: Moderation") dec(3) label


* 3) Pre en post Paris Agreement 
clear
use "EuropeDataset.dta"
gen interaction_popright = L3.popright_dummy * MNC
gen interaction_popleft = popleft_dummy * MNC
xtset IdentifierRIC_id year
eststo clear

eststo M1: xtreg ESGscore log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year <= 2015, fe vce(cluster IdentifierRIC_id)  
eststo M2: xtreg ESGscore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year <= 2015, fe vce(cluster IdentifierRIC_id) 
eststo M3: xtreg ESGscore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year <= 2015, fe vce(cluster IdentifierRIC_id) 
eststo M4: xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year <= 2015, fe vce(cluster IdentifierRIC_id) 
eststo M5: xtreg ESGscore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year <= 2015, fe vce(cluster IdentifierRIC_id) 

eststo M6: xtreg ESGscore log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year > 2015, fe vce(cluster IdentifierRIC_id)  
eststo M7: xtreg ESGscore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year > 2015, fe vce(cluster IdentifierRIC_id) 
eststo M8: xtreg ESGscore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year > 2015, fe vce(cluster IdentifierRIC_id) 
eststo M9: xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year > 2015, fe vce(cluster IdentifierRIC_id) 
eststo M10: xtreg ESGscore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if year > 2015, fe vce(cluster IdentifierRIC_id) 


esttab M1 M2 M3 M4 M5 M6 M7 M8 M9 M10 using regressionParisESG.rtf, replace b(%9.3f) se star(* 0.1 ** 0.05 *** 0.01)  title("Regression Results - Dependent Variable: ESG Score and before/ after 2015") mtitles("Model 1" "Model 2 " "Model 3" "Model 4" "Model 5" "Model 6 " "Model 7" "Model 8" "Model 9" "Model 10") label order(L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment) stats(r2 N N_g, fmt(3 0 0) labels("R-squared" "Observations" "Number of Firms"))


* 4) Gevoelige industrieen 
clear 
use "EuropeDataset.dta"
gen interaction_popright = L3.popright_dummy * MNC
gen interaction_popleft = popleft_dummy * MNC
eststo clear
xtset IdentifierRIC_id year

keep if inlist(industry, "Energy", "Materials", "Food, Beverage & Tobacco", "Pharmaceuticals, Biotechnology & Life Sciences") 

eststo M1: xtreg ESGscore log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)  
eststo M2: xtreg ESGscore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)  
eststo M3: xtreg ESGscore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)  
eststo M4: xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)  
eststo M5: xtreg ESGscore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id) 


outreg2 [M1 M2 M3 M4 M5] using gevoeligereg_uitkomsten.doc, replace se


esttab M1 M2 M3 M4 M5 using regression_sensitive.rtf, replace se b(%9.5f) star(* 0.1 ** 0.05 *** 0.01) label title("Regression Results - Sensitive Industries") mtitles("Model 1: Controls" "Model 2: IV1" "Model 3: IV2" "Model 4: IV1+2" "Model 5: Moderation") order(popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment) stats(r2 N N_g, fmt(3 0 0) labels("R-squared" "Observations" "Number of Firms")) 

* 5) Alleen landen met een populistische verleden
clear
use "EuropeDataset.dta"
xtset IdentifierRIC_id year
eststo clear
gen populist_past = 0 
replace populist_past = 1 if inlist(country, "Bulgaria", "Sweden", "Romania", "Netherlands", "Finland", "Austria", "Italy", "Poland") | inlist("Cyprus", "Czech Republic", "Portugal", "Denmark", "Spain", "Greece", "Estonia", "Hungary") | inlist("Latvia", "Lithuania", "Norway", "Slovakia", "Slovenia", "Switzerland", "United Kingdom")

xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment if populist_past == 1, fe vce(cluster IdentifierRIC_id) 

outreg2 using "reg_populistcountries_only.doc", replace ctitle("Populist Countries Only") dec(3)


* Model voorbeeld
clear 
use "EuropeDataset.dta"
gen interaction_popright = L3.popright_dummy * Foreign_Sales_Ratio
gen interaction_popleft = popleft_dummy * Foreign_Sales_Ratio
eststo clear
xtset IdentifierRIC_id year

eststo M1: xtreg ESGscore log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe 
eststo M2: xtreg ESGscore L3.popright_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe 
eststo M3: xtreg ESGscore popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe 
eststo M4: xtreg ESGscore L3.popright_dummy popleft_dummy log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe 
eststo M5: xtreg ESGscore L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ SolvencyRatio_ ROA_ PLbeforetax_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe 

esttab M1 M2 M3 M4 M5 using regression_moderator.rtf, replace se b(%9.5f) star(* 0.1 ** 0.05 *** 0.01) label title("Regression Results – Moderation by Foreign Sales Ratio") mtitles("Model 1: Controls" "Model 2: Popright" "Model 3: Popleft" "Model 4: Combined" "Model 5: Moderation") order(L3.popright_dummy popleft_dummy interaction_popright interaction_popleft log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment) stats(r2 N N_g, fmt(3 0 0) labels("R-squared" "Observations" "Number of Firms")) 


















// OVERIGE \\
// Regression imputation obv alle vars NIET MEENEMEN XXXXXXXXXX !!!!!
xtreg ESGscore log_OperatingRevenue log_TotalAssets i.industry_id i.year if !missing(ESGscore)
predict ESGscore_hat
replace ESGscore = ESGscore_hat if missing(ESGscore)

// Moderation dummy en conti
clear
use "EuropeDataset.dta"
gen interaction_cont = L3.popright_dummy * Foreign_Sales_Ratio

xtreg ESGscore L3.popright_dummy Foreign_Sales_Ratio interaction_cont log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)


clear
use "EuropeDataset.dta"
gen interaction_dummy = L3.popright_dummy * MNC

xtreg ESGscore L3.popright_dummy MNC interaction_dummy log_OperatingRevenue log_TotalAssets ROE_ ROA_ PLbeforetax_ SolvencyRatio_ FDI GDP Gross_Capital_Formation Inflation Unemployment, fe vce(cluster IdentifierRIC_id)







