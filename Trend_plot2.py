import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



Shampoo_data=pd.read_csv("shampoo.csv", parse_dates=['Month'],index_col='Month'
Trend_plot2=Shampoo_data.plot(figsize=(12,8));
plt.title=('Trend chart')
fig.figure.savefig('Shampoo_data_Trend_plot.png')
