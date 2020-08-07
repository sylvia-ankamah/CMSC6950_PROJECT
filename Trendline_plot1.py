import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymannkendall as mk

Birth_data = pd.read_csv("daily-total-female-births.csv",parse_dates=['Date'],index_col='Date')  #Birth_data
data = Birth_data

fig, ax = plt.subplots(figsize=(12, 8))
res = mk.original_test(data)
trend_line = np.arange(len(data)) * res.slope + res.intercept

ax.plot(data)
ax.plot(data.index, trend_line)
ax.legend(['data', 'trend line'])
ax.set(xlabel= "Dates", ylabel= "Births", title="Trend line")
fig.savefig('Trendline_plot1.png')
