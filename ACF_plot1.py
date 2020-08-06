import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Birth_data = pd.read_csv("daily-total-female-births.csv",parse_dates=['Date'],index_col='Date')  #Birth_data
fig, ax = plt.subplots(figsize=(12, 8))
fig_2 =sm.graphics.tsa.plot_acf(Birth_data, lags=20, ax=ax);
ax.set(xlabel= "Dates", ylabel= "Births", title="AUTOCORRELATION")
fig_2.savefig('ACF_plot1.png')


