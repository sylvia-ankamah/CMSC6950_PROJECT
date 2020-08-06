
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Shampoo_data=pd.read_csv("shampoo.csv", parse_dates=['Month'],index_col='Month')
fig, ax = plt.subplots(figsize=(12, 8))
sm.graphics.tsa.plot_acf(Shampoo_data, lags=20, ax=ax);
ax.set(xlabel= "Months", ylabel= "Sales", title="AUTOCORRELATION")
fig.savefig('SHAMPOO_DATA_ACF_PLOT.png')
