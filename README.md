#
 CMSC6950:MANNKENDALL TREND TEST

# SYLVIA ANKAMAH

Software:https://github.com/mmhs013/pyMannKendall

Paper:Hussain et al., (2019). pyMannKendall: a python package for non parametric Mann Kendall family of trend tests.. Journal of Open Source Software, 4(39), 1556. https://doi.org/10.21105/joss.01556

Data Source:

daily-total-female-births.csv

shampoo.csv

Malaria_data.csv


# Dependencies

1.Matplotlib
i
2.Pandas

3.Numpy

4.Statsmodels

# pyMannKendall Test

pyMannkendal is a pure Python implementation of non-parametric Mann-Kendall trend analysis, which bring together almost all types of Mann-Kendall Test (Hussain et al., 2019). Currently, this package has 11 Mann-Kendall Tests and 2 sen's slope estimator function. Brief description of functions are below:

1. Original Mann-Kendall test (original_test): Original Mann-Kendall test is a nonparametric test, which does not consider serial correlation or seasonal effects.

2. Hamed and Rao Modified MK Test (hamed_rao_modification_test): This modified MK test proposed by Hamed and Rao (1998) to address serial autocorrelation issues. They suggested a variance correction approach to improve trend analysis. User can consider first n significant lag by insert lag number in this function. By default, it considered all significant lags.

3. Yue and Wang Modified MK Test (yue_wang_modification_test): This is also a variance correction method for considered serial autocorrelation proposed by Yue, & Wang (2004). User can also set their desired significant n lags for the calculation.

4. Modified MK test using Pre-Whitening method (pre_whitening_modification_test): This test suggested by Yue and Wang (2002) to using Pre-Whitening the time series before the application of trend test.

5. Modified MK test using Trend free Pre-Whitening method (trend_free_pre_whitening_modification_test): This test also proposed by Yue and Wang (2002) to remove trend component and then Pre-Whitening the time series before application of trend test.

6. Multivariate MK Test (multivariate_test): This is an MK test for multiple parameters proposed by Hirsch (1982). He used this method for seasonal mk test, where he considered every month as a parameter.

7. Seasonal MK Test (seasonal_test): For seasonal time series data, Hirsch, Slack and Smith (1982) proposed this test to calculate the seasonal trend.

8. Regional MK Test (regional_test): Based on Hirsch (1982) proposed seasonal mk test, Helsel and Frans (2006) suggest regional mk test to calculate the overall trend in a regional scale.

9. Correlated Multivariate MK Test (correlated_multivariate_test): This multivariate mk test proposed by Hipel (1994) where the parameters are correlated.

10. Correlated Seasonal MK Test (correlated_seasonal_test): This method proposed by Hipel (1994) used, when time series significantly correlated with the preceding one or more months/seasons.

11. Partial MK Test (partial_test): In a real event, many factors are affecting the main studied response parameter, which can bias the trend results. To overcome this problem, Libiseller (2002) proposed this partial mk test. It required two parameters as input, where, one is response parameter and other is an independent parameter.

12. Theil-Sen's Slope Estimator (sens_slope): This method proposed by Theil (1950) and Sen (1968) to estimate the magnitude of the monotonic trend. Intercept is calculate using Conover, W.J. (1980) method.

13. Seasonal Theil-Sen's Slope Estimator (seasonal_sens_slope): This method proposed by Hipel (1994) to estimate the magnitude of the monotonic trend, when data has seasonal effects. Intercept is calculate using Conover (1980) method.

# Function details:
All Mann-Kendall test functions have almost similar input parameters. These are:

x: a vector (list, numpy array or pandas series) data

alpha: significance level (0.05 is the default)

lag: No. of First Significant Lags (Only available in hamed_rao_modification_test and yue_wang_modification_test)

period: seasonal cycle. For monthly data it is 12, weekly data it is 52 (Only available in seasonal tests)


And all Mann-Kendall tests return a named tuple which contained:

trend: tells the trend (increasing, decreasing or no trend)

h: True (if trend is present) or False (if the trend is absence)

p: p-value of the significance test

z: normalized test statistics

Tau: Kendall Tau

s: Mann-Kendal's score

var_s: Variance S

slope: Theil-Sen estimator/slope

intercept: intercept of Kendall-Theil Robust Line, for seasonal test, full period cycle consider as unit time step


sen's slope function required data vector. seasonal sen's slope also has optional input period, which by the default value is 12. Both sen's slope function return only slope value.

# INSTALLATION
You can install pyMannKendall using pip.

 For Linux users

sudo pip install pymannkendall

or, for Windows user

pip install pymannkendall

Or you can clone the repo and install it:

git clone https://github.com/mmhs013/pymannkendall

cd pymannkendall

python setup.py install

# Reference
1. Hamed, K. H., & Rao, A. R. (1998). A modified Mann-Kendall trend test for autocorrelated data. Journal of hydrology, 204(1-4), 182-196. doi:10.1016/S0022-1694(97)00125-X

2. Hipel, K. W., & McLeod, A. I. (1994). Time series modelling of water resources and environmental systems (Vol. 45). Elsevier.

3. Hirsch, R. M., Slack, J. R., & Smith, R. A. (1982). Techniques of trend analysis for monthly water quality data. Water resources research, 18(1), 107-121. doi:10.1029/WR018i001p00107

4. Hussain et al., (2019). pyMannKendall: a python package for non parametric Mann Kendall family of trend tests. Journal of Open Source Software, 4(39), 1556, https://doi.org/10.21105/joss.01556

5. Libiseller, C., & Grimvall, A. (2002). Performance of partial Mann-Kendall tests for trend detection in the presence of covariates. Environmetrics: The official journal of the International Environmetrics Society, 13(1), 71-84. doi:10.1002/env.507

6. Sen, P. K. (1968). Estimates of the regression coefficient based on Kendall's tau. Journal of the American statistical association, 63(324), 1379-1389. doi:10.1080/01621459.1968.10480934

7. Theil, H. (1950). A rank-invariant method of linear and polynominal regression analysis (parts 1-3). In Ned. Akad. Wetensch. Proc. Ser. A (Vol. 53, pp. 1397-1412).

8. Yue, S., & Wang, C. (2004). The Mann-Kendall test modified by effective sample size to detect trend in serially correlated hydrological series. Water resources management, 18(3), 201-218. doi:10.1023/B:WARM.0000043140.61082.60

9. Yue, S., & Wang, C. Y. (2002). Applicability of prewhitening to eliminate the influence of serial correlation on the Mann-Kendall test. Water resources research, 38(6), 4-1. doi:10.1029/2001WR000861

