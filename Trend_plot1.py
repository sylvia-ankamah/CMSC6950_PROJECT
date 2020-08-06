
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


Birth_data = pd.read_csv("daily-total-female-births.csv",parse_dates=['Date'],index_col='Date')  #Birth_data
fig_1=Birth_data.plot(figsize=(12,8));
plt.title = ('Trend test')
fig_1.figure.savefig('Trend_plot1.png')

