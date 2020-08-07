# CMSC6950 PROJECT

# STEP 1
import numpy as np
import pandas as pd
import pymannkendall as mk
import matplotlib.pyplot as plt
import statsmodels.api as sm


# IMPORTING THE FIRST DATA SET
Birth_data = pd.read_csv("daily-total-female-births.csv",parse_dates=['Date'],index_col='Date')

# SUMMARY STATISTICS
head=Birth_data.head()
Summary=Birth_data.describe()
print(head)
print(Summary)


# MANNKENDALL TREND TEST
Birth_data = pd.read_csv("daily-total-female-births.csv",parse_dates=['Date'],index_col='Date')  #Birth_data
MKT=mk.original_test(Birth_data, alpha=0.05)
print(MKT)


# IMPORTING SECOND DATA SET
Shampoo_data=pd.read_csv("shampoo.csv", parse_dates=['Month'],index_col='Month')

# SUMMARY STATISTICS
head_shampoo=Shampoo_data.head()
Summary_shampoo=Shampoo_data.describe()
print(head_shampoo)
print(Summary_shampoo)


# TREND TEST 1
MKT1=mk.hamed_rao_modification_test(Shampoo_data)
print(MKT1)

# TREND TEST 2
MKT2=mk.yue_wang_modification_test(Shampoo_data)
print(MKT2)

# TREND TEST 3
MKT3=mk.trend_free_pre_whitening_modification_test(Shampoo_data)
print(MKT3)



# IMPORTING THIRD DATA
Malaria_data = pd.read_csv("Malaria_data.csv",parse_dates=['Date'],index_col='Date')

# SUMMARY STATISTICS
Malaria_head=Malaria_data.head()
Malaria_summary=Malaria_data.describe()
print(Malaria_head)
print(Malaria_summary)


#TREND TEST
MKT4=mk.hamed_rao_modification_test(Malaria_data)
print(MKT4)
 
