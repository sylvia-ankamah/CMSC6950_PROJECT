
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


Malaria_data = pd.read_csv("Malaria_data.csv",parse_dates=['Date'],index_col='Date')
fig, ax = plt.subplots(figsize=(12, 8))                                                                                                                                 sm.graphics.tsa.plot_acf(Malaria_data, lags=20, ax=ax);                                                                                                                 ax.set(xlabel= "Years", ylabel= "Malaria cases", title="AUTOCORRELATION")                                                                                               fig.savefig('MALARIA_DATA_ACF_PLOT.png') 
