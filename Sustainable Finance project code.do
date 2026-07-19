* Part 1: Preparing dataset 
clear all 
set maxvar 15000
cd "/Users/morrisdelange_1/Downloads"
import excel "Data_Ass" ,sheet ("Return") cellrange(B2:IH3036)
xpose, clear
forvalues i = 1/3035{
rename v`i' R`i'
} 
gen time =_n
save Data_Ass, replace 

clear all
import excel "Data_Ass", sheet ("ME (Mil)") cellrange(B2:IH3036)
xpose, clear 
forvalues i = 1/3035{
rename v`i' ME`i' 
}
gen time =_n
merge 1:1 time using Data_Ass.dta 
drop _merge 
save Data_Ass, replace 

clear all
import excel "Data_Ass", sheet ("Env") cellrange(B2:IH3036)
xpose, clear
forvalues i = 1/3035{
	rename v`i' Env`i'
}
gen time =_n 
merge 1:1 time using Data_Ass.dta 
drop _merge
save Data_Ass, replace

clear all
import excel "Data_Ass.xlsx", sheet("Factors") cellrange(B5:IH5) // Import RF row
xpose, clear // Transpose to make each column a variable
rename v1 RF // Rename the variable to RF (Risk-Free Rate)
gen time = _n // Generate time variable (assuming it aligns with existing dataset)
merge 1:1 time using "Data_Ass.dta" // Merge with your main dataset by 'time'
drop _merge // Remove merge status indicator
save "Data_Ass.dta", replace // Save the updated dataset

clear
use Data_Ass.dta
reshape long ME Env R, i(time) 
rename _j stock
sort stock time
save Data_Ass_R, replace 

clear 
use Data_Ass_R 
drop if missing(R)
drop if missing(Env) 
drop if missing(RF)

* Part 2: Analysis 
gen R1 = .
gen R2 = . 
gen R3 = .
gen R4 = . 
gen R5 = .
gen Env1 = . 
gen Env2 = . 
gen Env3 = . 
gen Env4 = . 
gen Env5 = . 
forvalues t = 1/241{
	centile Env, centile(20 40 60 80), if time == `t'
	gen P1 = Env <= r(c_1) if time == `t'
	gen P2 = Env > r(c_1) & Env <= r(c_2) if time == `t'
	gen P3 = Env > r(c_2) & Env <= r(c_3) if time == `t'
	gen P4 = Env > r(c_3) & Env <= r(c_4) if time == `t'
	gen P5 = Env > r(c_4) if time == `t'
* Exlcude the firms without an environmental score	
	replace P1 = . if missing(Env)
	replace P2 = . if missing(Env)
	replace P3 = . if missing(Env)
	replace P4 = . if missing(Env)
	replace P5 = . if missing(Env)
* Compute the total market cap per portfolio
	sum ME if P1 == 1 & time == `t'
	scalar Sum1 = r(sum)
	sum ME if P2 == 1 & time == `t'
	scalar Sum2 = r(sum)
	sum ME if P3 == 1 & time == `t'
	scalar Sum3 = r(sum)
	sum ME if P4 == 1 & time == `t'
	scalar Sum4 = r(sum)
	sum ME if P5 == 1 & time == `t'
	scalar Sum5 = r(sum)
* Compute the weights of the sotcks in each portfolio
	gen W1 = ME/Sum1 if P1 == 1 & time ==`t'
	gen W2 = ME/Sum2 if P2 == 1 & time ==`t'
	gen W3 = ME/Sum3 if P3 == 1 & time ==`t'
	gen W4 = ME/Sum4 if P4 == 1 & time ==`t'
	gen W5 = ME/Sum5 if P5 == 1 & time ==`t'
* Compute the portfolio returns
	replace R1 = R*W1 if P1 == 1 & time == `t'
	replace R2 = R*W2 if P2 == 1 & time == `t'
	replace R3 = R*W3 if P3 == 1 & time == `t'
	replace R4 = R*W4 if P4 == 1 & time == `t'
	replace R5 = R*W5 if P5 == 1 & time == `t'
* Compute the portfolio environmetal
	replace Env1 = Env*W1 if P1 == 1 & time == `t'
	replace Env2 = Env*W2 if P2 == 1 & time == `t'
	replace Env3 = Env*W3 if P3 == 1 & time == `t'
	replace Env4 = Env*W4 if P4 == 1 & time == `t'
	replace Env5 = Env*W5 if P5 == 1 & time == `t'
* Drop the portfolio and weight variables because
* they are nit useful anymore
	drop P* W* 
} 

collapse (sum) R1 R2 R3 R4 R5 Env1 Env2 Env3 Env4 Env5, by (time) 

save Data_Portfolios, replace 

*Tutorial 2*

clear 
import excel using Data.xlsx, sheet("Factors") cellrange(B2:IH5)
xpose, clear

rename v1 Mkt
rename v2 SMB
rename v3 HML 
rename v4 Rf

gen time =_n

* Merge the two datasets 
merge 1:1 time using Data_Portfolios.dta

drop _merge 

* Compute the excess returns (Ex) 
forvalues i = 1/5{
	
	cap no gen Ex`i' = R`i' - Rf 
}

drop R*

save Data_Portfolios, replace 

// Descriptive statistics 
clear 
use Data_Portfolios 

// Reshape the portfolio returns 
reshape long Ex Env, i(time) j(port) // Correct reshape syntax
sort port time

replace Ex = Ex * 100

gen Avg_Ex = .
gen Std = .
gen Avg_Env = .

forvalues i = 1/5 { // Loop through portfolios
    // Summary statistics for Ex
    sum Ex if port == `i'
    replace Avg_Ex = r(mean) if port == `i'
    replace Std = r(sd) if port == `i'

    // Summary statistics for Env
    sum Env if port == `i'
    replace Avg_Env = r(mean) if port == `i'
}

// Compute Sharpe ratio
gen ShR = Avg_Ex / Std

collapse (mean) Avg_Ex Std ShR Avg_Env, by (port)
export excel using Results_Desc.xlsx, firstrow(variables) keepcellfmt replace 

* Estimate CAPM
clear s
clear matrix 
use Data_Portfolios

* Reshape the portfolio returns
reshape long Ex Env, i(time) j(port) // Correct reshape syntax
sort port time

* Estimate the CAPM to retrieve the alphas and the market betas
gen Alpha = 0
gen Beta_Mk = 0
gen t_Alpha = 0 
gen t_Mk = 0
gen P_Alpha = 0

forvalues i = 1/5 { // Correct loop syntax
    reg Ex Mkt if port == `i' // Regression for each portfolio
    replace Alpha = _b[_cons] if port == `i'
    replace Beta_Mk = _b[Mkt] if port == `i'
    replace t_Alpha = _b[_cons] / _se[_cons] if port == `i' // Correct `_se[_cons ]` syntax
    replace t_Mk = _b[Mkt] / _se[Mkt] if port == `i' // Correct t-stat for Beta_Mk
    replace P_Alpha = 2 * ttail(e(df_r), abs(t_Alpha)) if port == `i' // Correct degrees of freedom and logical condition
}

replace Alpha = Alpha * 100

collapse (mean) Env Alpha t_Alpha P_Alpha Beta_Mk t_Mk, by(port)

* Estimate FF
clear 
clear matrix 
use Data_Portfolios

* Reshape the portfolio returns
reshape long Ex Env, i(time) j(port) // Correct reshape syntax
sort port time

* Estimate the FF to retrieve the alphas and the market betas
gen Alpha = 0
gen Beta_Mk = 0
gen Beta_SMB = 0
gen Beta_HML = 0
gen t_Alpha = 0
gen t_Mk = 0
gen t_SMB = 0
gen t_HML = 0
gen P_Alpha = 0

forvalues i = 1/5 { 
    reg Ex Mkt SMB HML if port == `i' // Fama-French regression for each portfolio
    replace Alpha = _b[_cons] if port == `i'
    replace Beta_Mk = _b[Mkt] if port == `i'
    replace Beta_SMB = _b[SMB] if port == `i'
    replace Beta_HML = _b[HML] if port == `i'
    
    // Compute t-statistics
    replace t_Alpha = _b[_cons] / _se[_cons] if port == `i'
    replace t_Mk = _b[Mkt] / _se[Mkt] if port == `i'
    replace t_SMB = _b[SMB] / _se[SMB] if port == `i'
    replace t_HML = _b[HML] / _se[HML] if port == `i'
	
	replace P_Alpha = 2*ttail(e(N)-1,abs(t_Alpha)) if port ==`i'
}

replace Alpha = Alpha * 100
collapse (mean) Env Alpha t_Alpha P_Alpha Beta_Mk t_Mk Beta_SMB t_SMB Beta_HML t_HML, by(port) 

export excel using question3.xlsx, firstrow(variables) keepcellfmt replace 
