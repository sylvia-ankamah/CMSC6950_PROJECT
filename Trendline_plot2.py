import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymannkendall as mk

Shampoo_data=pd.read_csv("shampoo.csv", parse_dates=['Month'],index_col='Month')
data = Shampoo_data

fig, ax = plt.subplots(figsize=(12, 8))
res = mk.hamed_rao_modification_test(data)
trend_line = np.arange(len(data)) * res.slope + res.intercept

ax.plot(data)
ax.plot(data.index, trend_line)
ax.legend(['data', 'trend line'])
ax.set(xlabel= "Months", ylabel= "Sales", title="TREND LINE")
fig.savefig('SHAMPOO_DATA_TRENDLINE.png')
