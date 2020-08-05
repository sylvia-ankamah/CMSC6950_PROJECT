# CMSC6950 PROJECT

# STEP 1
import numpy as np
import pandas as pd
import pymannkendall as mk
import matplotlib.pyplot as plt
%matplotlib inline
import statsmodels.api as sm

# IMPORTING THE FIRST DATA SET
Birth_data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-total-female-births.csv",parse_dates=['Date'],index_col='Date')

# SUMMARY STATISTICS
Birth_data.head()
# GRAPH 1
Birth_data.plot(figsize=(12,8));
# GRAPH 2
fig, ax = plt.subplots(figsize=(12, 8))
sm.graphics.tsa.plot_acf(Birth_data, lags=20, ax=ax)

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


# IMPORTING SECOND DATA SET
Shampoo_data=pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv", parse_dates=['Month'],index_col='Month')

# SUMMARY STATISTICS
Shampoo_data.head()

# GRAPH 1
Shampoo_data.plot(figsize=(12,8));
# GRAPH 2

fig, ax = plt.subplots(figsize=(12, 8))
sm.graphics.tsa.plot_acf(Shampoo_data, lags=20, ax=ax);

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




