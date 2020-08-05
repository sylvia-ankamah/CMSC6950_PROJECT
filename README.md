# CMSC6950:MANNKENDALL TREND TEST

# SYLVIA ANKAMAH

Software:https://github.com/mmhs013/pyMannKendall

Paper:Hussain et al., (2019). pyMannKendall: a python package for non parametric Mann Kendall family of trend tests.. Journal of Open Source Software, 4(39), 1556. https://doi.org/10.21105/joss.01556

Data Source:
daily-total-female-births.csv
shampoo.csv
Malaria_data.csv


# Dependencies

1.Matplotlib

2.Pandas

3.Numpy

4.Statsmodels

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
