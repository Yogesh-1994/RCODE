# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:11:54 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Company_Data =pd.read_csv("C:\\Users\\Yogesh\\Downloads\\Company_Data.csv")
Company_Data.head(40)
Company_Data.corr()
import seaborn as sns
sns.pairplot(Company_Data)
Company_Data.columns
import statsmodels.formula.api as smf
ml1 = smf.ols('Sales~CompPrice+Income+Advertising+Population+Price+Age+Education',data=Company_Data).fit()
ml1.params
ml1.summary()
ml_v=smf.ols('Sales~CompPrice',data=Company_Data).fit()
ml_v.summary()
ml_w=smf.ols('Sales~Income',data=Company_Data).fit()
ml_w.summary()
ml_p=smf.ols('Sales~Population',data=Company_Data).fit()
ml_p.summary()
ml_a=smf.ols('Sales~Age',data=Company_Data).fit()
ml_a.summary()
ml_vwpa=smf.ols('Sales~CompPrice+Income+Population+Age',data=Company_Data).fit()
ml_vwpa.summary()
import statsmodels.api as sm
sm.graphics.influence_plot(ml1)
Company_Data_new=Company_Data.drop(Company_Data.index[[76,78]],axis=0)
ml_new=smf.ols('Sales~CompPrice+Income+Advertising+Population+Price+Age+Education',data=Company_Data_new).fit()
ml_new.params
ml_new.summary()
print(ml_new.conf_int(0.01))
mpg_pred=ml_new.predict(Company_Data_new[['CompPrice','Income','Advertising','Population','Price','Age','Education']])
mpg_pred
Company_Data_new.head()
rsq_compprice=smf.ols('CompPrice~Income+Population+Age',data=Company_Data_new).fit().rsquared
vif_compprice=1/(1-rsq_compprice)
rsq_income=smf.ols('Income~CompPrice+Population+Age',data=Company_Data_new).fit().rsquared
vif_income=1/(1-rsq_income)
rsq_population=smf.ols('Population~CompPrice+Income+Age',data=Company_Data_new).fit().rsquared
vif_population=1/(1-rsq_population)
rsq_age=smf.ols('Age~CompPrice+Income+Population',data=Company_Data_new).fit().rsquared
vif_age=1/(1-rsq_age)
d1={'variables':['CompPrice','Income','Population','Age'],'VIF':[vif_compprice,vif_income,vif_population,vif_age]}
Vif_frame=pd.DataFrame(d1)
Vif_frame
sm.graphics.plot_partregress_grid(ml_new)
import statsmodels.api as sm
final_ml=smf.ols('Sales~Population+Age+CompPrice',data=Company_Data_new).fit()
final_ml.params
final_ml.summary()
sales_pred=final_ml.predict(Company_Data_new)
import statsmodels.api as sm
sm.graphics.plot_partregress_grid(final_ml)
plt.scatter(Company_Data_new.Sales,sales_pred,c="r");plt.xlabel("Observed_values");plt.ylabel("Fitted_values")
plt.scatter(sales_pred,final_ml.resid_pearson,c="r"),plt.axhline(y=0,color="blue");plt.xlabel("Fitted_values")
plt.hist(final_ml.resid_pearson)
import pylab
import scipy.stats as st
st.probplot(final_ml.resid_pearson,dist="norm",plot=pylab)
plt.scatter(sales_pred,final_ml.resid_pearson,c="r"),plt.axhline(y=0,color="blue");plt.xlabel("Fitted_values");plt.ylabel("residuals")
from sklearn.model_selection import train_test_split
Company_Data_train,Company_Data_test=train_test_split(Company_Data_new,test_size=0.2)
model_train=smf.ols("Sales~CompPrice+Age+Population",data=Company_Data_train).fit()
train_pred=model_train.predict(Company_Data_train)
train_resid =train_pred - Company_Data_train.Sales
train_rmse=np.sqrt(np.mean(train_resid*train_resid))
test_pred=model_train.predict(Company_Data_test)
test_resid=test_pred - Company_Data_test.Sales
test_rmse=np.sqrt(np.mean(test_resid*test_resid))
