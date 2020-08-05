# CMSC6950 PROJECT

# STEP 1
import numpy as np
import pandas as pd
import pymannkendall as mk
import matplotlib.pyplot as plt
%matplotlib inline
import statsmodels.api as sm

# IMPORTING THE FIRST DATA SET
Birth_data = pd.read_csv("daily-total-female-births.csv",parse_dates=['Date'],index_col='Date')

# SUMMARY STATISTICS
Birth_data.head()
Birth_data.describe()

# GRAPH 1

fig_1=Birth_data.plot(figsize=(12,8));
plt.title = ('Trend test')
fig_1.figure.savefig('Birth_data_Trend_plot.png')

# GRAPH 2

fig, ax = plt.subplots(figsize=(12, 8))
fig_2 =sm.graphics.tsa.plot_acf(Birth_data, lags=20, ax=ax);
ax.set(xlabel= "Dates", ylabel= "Births", title="AUTOCORRELATION")
fig_2.savefig('BIRTH_DATA_ACF_PLOT.png')sm.graphics.tsa.plot_acf(Birth_data, lags=20, ax=ax)

# MANNKENDALL TREND TEST
mk.original_test(Birth_data, alpha=0.05)

# Graph 3
data = Birth_data

fig, ax = plt.subplots(figsize=(12, 8))
res = mk.original_test(data)
trend_line = np.arange(len(data)) * res.slope + res.intercept

ax.plot(data)
ax.plot(data.index, trend_line)
ax.legend(['data', 'trend line'])
ax.set(xlabel= "Dates", ylabel= "Births", title="Trend line")
fig.savefig('Birth_data_Trendline.png')


# IMPORTING SECOND DATA SET
Shampoo_data=pd.read_csv("shampoo.csv", parse_dates=['Month'],index_col='Month')

# SUMMARY STATISTICS
Shampoo_data.head()
Shampoo_data.describe()

# GRAPH 1
fig_3=Shampoo_data.plot(figsize=(12,8));
plt.title=('Trend chart')
fig_3.figure.savefig('Shampoo_data_Trend_plot.png')

# GRAPH 2
fig, ax = plt.subplots(figsize=(12, 8))
sm.graphics.tsa.plot_acf(Shampoo_data, lags=20, ax=ax);
ax.set(xlabel= "Months", ylabel= "Sales", title="AUTOCORRELATION")
fig.savefig('SHAMPOO_DATA_ACF_PLOT.png')

# TREND TEST 1
mk.hamed_rao_modification_test(Shampoo_data)

# TREND TEST 2
mk.yue_wang_modification_test(Shampoo_data)

# TREND TEST 3
mk.trend_free_pre_whitening_modification_test(Shampoo_data)

#GRAPH 3
data = Shampoo_data

fig, ax = plt.subplots(figsize=(12, 8))
res = mk.hamed_rao_modification_test(data)
trend_line = np.arange(len(data)) * res.slope + res.intercept

ax.plot(data)
ax.plot(data.index, trend_line)
ax.legend(['data', 'trend line'])
ax.set(xlabel= "Months", ylabel= "Sales", title="TREND LINE")
fig.savefig('SHAMPOO_DATA_TRENDLINE.png')

# IMPORTING THIRD DATA
Malaria_data = pd.read_csv("Malaria_data.csv",parse_dates=['Date'],index_col='Date')

# SUMMARY STATISTICS
 Malaria_data.head()
Malaria_data.describe()
# GRAPH 1
fig_4=Malaria_data.plot(figsize=(12,8))
plt.title=('Trend chart')
fig_4.figure.savefig('Malaria_Trend_plot.png')

# GRAPH 2
fig, ax = plt.subplots(figsize=(12, 8))
sm.graphics.tsa.plot_acf(Malaria_data, lags=20, ax=ax);
ax.set(xlabel= "Years", ylabel= "Malaria cases", title="AUTOCORRELATION")
fig.savefig('MALARIA_DATA_ACF_PLOT.png')

#TREND TEST
mk.hamed_rao_modification_test(Malaria_data)

