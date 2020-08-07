
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


Malaria_data = pd.read_csv("Malaria_data.csv")
fig, ax = plt.subplots(figsize=(12, 8))                                                                                 sm.graphics.tsa.plot_acf(Malaria_data, lags=20, ax=ax);                                                                 ax.set(xlabel= "Years", ylabel= "Malaria cases", title="AUTOCORRELATION")                                               fig.savefig('MALARIA_DATA_ACF_PLOT.png') 
