import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


Malaria_data = pd.read_csv("Malaria_data.csv",parse_dates=['Date'],index_col='Date')
fig_4=Malaria_data.plot(figsize=(12,8))
plt.title=('Trend chart')
fig_4.figure.savefig('Malaria_Trend_plot.png')


