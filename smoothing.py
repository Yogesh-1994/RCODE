# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 21:25:57 2020

@author: hp
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import SimpleExpSmoothing # SES
from statsmodels.tsa.holtwinters import Holt # Holts Exponential Smoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing # 
#from datetime import datetime,time
#from sm.tsa.statespace import sa
Amtrak = pd.read_csv("C:\\Users/\Yogesh\\Desktop\\Walmart Footfalls Raw.csv")

#Amtrak.rename(columns={"Footfalls":"Footfalls"},inplace=True)   
# Converting the normal index of Amtrak to time stamp 


Amtrak.Footfalls.plot() # time series plot 
# Creating a Date column to store the actual Date format for the given Month column
Amtrak["Date"] = pd.to_datetime(Amtrak.Month,format="%b-%y")
#look for c standard format codes

# Extracting Day, weekday name, month name, year from the Date column using 
# Date functions from pandas 

Amtrak["month"] = Amtrak.Date.dt.strftime("%b") # month extraction
#Amtrak["Day"] = Amtrak.Date.dt.strftime("%d") # Day extraction
#Amtrak["wkday"] = Amtrak.Date.dt.strftime("%A") # weekday extraction
Amtrak["year"] = Amtrak.Date.dt.strftime("%Y") # year extraction

# Some EDA on Time series data 
# Heat map visualization 
#heatmap_y_month = pd.pivot_table(data=Amtrak,values="Footfalls",index="year",columns="month",aggfunc="mean",fill_value=0)
#sns.heatmap(heatmap_y_month,annot=True,fmt="g")

# Boxplot for ever
sns.boxplot(x="month",y="Footfalls",data=Amtrak)
sns.boxplot(x="year",y="Footfalls",data=Amtrak)
# sns.factorplot("month","Ridership",data=Amtrak,kind="box")

# Line plot for Ridership based on year
sns.lineplot(x="year",y="Footfalls",data=Amtrak)


# Centering moving average for the time series to understand better about the trend character in Amtrak
Amtrak.Footfalls.plot(label="org")
for i in range(2,24,6):
    Amtrak["Footfalls"].rolling(i).mean().plot(label=str(i))
plt.legend(loc=3)
    
# Time series decomposition plot 
decompose_ts_add = seasonal_decompose(Amtrak.Footfalls,model="additive",period=12)
decompose_ts_add.plot()
decompose_ts_mul = seasonal_decompose(Amtrak.Footfalls,model="multiplicative",period=12)
decompose_ts_mul.plot()

# ACF plots and PACF plots on Original data sets 
import statsmodels.graphics.tsaplots as tsa_plots
tsa_plots.plot_acf(Amtrak.Footfalls,lags=12)
tsa_plots.plot_pacf(Amtrak.Footfalls,lags=12)

# Amtrak.index.freq = "MS" 
# splitting the data into Train and Test data and considering the last 12 months data as 
# Test data and left over data as train data 

Train = Amtrak.head(147)
Test = Amtrak.tail(12)
# to change the index value in pandas data frame 
# Test.set_index(np.arange(1,13),inplace=True)

# Creating a function to calculate the MAPE value for test data 
def MAPE(pred,org):
    temp = np.abs((pred-org)/org)*100
    return np.mean(temp)


# Simple Exponential Method
ses_model = SimpleExpSmoothing(Train["Footfalls"]).fit()
pred_ses = ses_model.predict(start = Test.index[0],end = Test.index[-1])
MAPE(pred_ses,Test.Footfalls) # 7.846321

# Holt method 
hw_model = Holt(Train["Footfalls"]).fit()
pred_hw = hw_model.predict(start = Test.index[0],end = Test.index[-1])
MAPE(pred_hw,Test.Footfalls) # 7.261176729658341

# Holts winter exponential smoothing with additive seasonality and additive trend
hwe_model_add_add = ExponentialSmoothing(Train["Footfalls"],seasonal="add",trend="add",seasonal_periods=12).fit()
pred_hwe_add_add = hwe_model_add_add.predict(start = Test.index[0],end = Test.index[-1])
MAPE(pred_hwe_add_add,Test.Footfalls) # 4.500954

hwe_model_add_add = ExponentialSmoothing(Amtrak["Footfalls"],seasonal="add",trend="add",seasonal_periods=12).fit()
pred_hwe_add_add = hwe_model_add_add.predict(start = Amtrak.index[0],end = Amtrak.index[-1])


# Holts winter exponential smoothing with multiplicative seasonality and additive trend
hwe_model_mul_add = ExponentialSmoothing(Train["Footfalls"],seasonal="mul",trend="add",seasonal_periods=12).fit()
pred_hwe_mul_add = hwe_model_mul_add.predict(start = Test.index[0],end = Test.index[-1])
MAPE(pred_hwe_mul_add,Test.Footfalls) # 4.109309


plt.plot(Train.index, Train["Footfalls"], label='Train',color="black")
plt.plot(Test.index, Test["Footfalls"], label='Test',color="blue")
plt.plot(pred_ses.index, pred_ses, label='SimpleExponential',color="green")
plt.plot(pred_hw.index, pred_hw, label='Holts_winter',color="red")
plt.plot(pred_hwe_add_add.index,pred_hwe_add_add,label="HoltsWinterExponential_1",color="brown")
plt.plot(pred_hwe_mul_add.index,pred_hwe_mul_add,label="HoltsWinterExponential_2",color="yellow")