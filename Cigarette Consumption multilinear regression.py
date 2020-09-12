# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:11:54 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
CigaretteConsumption =pd.read_csv("C:\\Users\\Yogesh\\Downloads\\CigaretteConsumption.csv")
CigaretteConsumption.head(40)
CigaretteConsumption.corr()
import seaborn as sns
sns.pairplot(CigaretteConsumption)
CigaretteConsumption.columns
import statsmodels.formula.api as smf
ml1 = smf.ols('Sales~Age+HS+Income+Black+Female+Price',data=CigaretteConsumption).fit()
ml1.params
ml1.summary()
ml_v=smf.ols('Sales~Age',data=CigaretteConsumption).fit()
ml_v.summary()
ml_w=smf.ols('Sales~Income',data=CigaretteConsumption).fit()
ml_w.summary()
ml_p=smf.ols('Sales~HS',data=CigaretteConsumption).fit()
ml_p.summary()
ml_a=smf.ols('Sales~Female',data=CigaretteConsumption).fit()
ml_a.summary()
ml_vwpa=smf.ols('Sales~Age+Income+HS+Female',data=CigaretteConsumption).fit()
ml_vwpa.summary()
import statsmodels.api as sm
sm.graphics.influence_plot(ml1)
CigaretteConsumption_new=CigaretteConsumption.drop(CigaretteConsumption.index[[48,50]],axis=0)
ml_new=smf.ols('Sales~Age+HS+Income+Black+Female+Price',data=CigaretteConsumption_new).fit()
ml_new.params
ml_new.summary()
print(ml_new.conf_int(0.01))
mpg_pred=ml_new.predict(CigaretteConsumption_new[['Age','HS','Income','Black','Female','Price',]])
mpg_pred
CigaretteConsumption_new.head()
rsq_age=smf.ols('Age~Income+HS+Female',data=CigaretteConsumption_new).fit().rsquared
vif_age=1/(1-rsq_age)
rsq_income=smf.ols('Income~Age+HS+Female',data=CigaretteConsumption_new).fit().rsquared
vif_income=1/(1-rsq_income)
rsq_hs=smf.ols('HS~Age+Income+Female',data=CigaretteConsumption_new).fit().rsquared
vif_hs=1/(1-rsq_hs)
rsq_female=smf.ols('Female~Age+Income+HS',data=CigaretteConsumption_new).fit().rsquared
vif_female=1/(1-rsq_female)
d1={'variables':['Age','Income','HS','Female'],'VIF':[vif_age,vif_income,vif_hs,vif_female]}
Vif_frame=pd.DataFrame(d1)
Vif_frame
sm.graphics.plot_partregress_grid(ml_new)
import statsmodels.api as sm
final_ml=smf.ols('Sales~HS+Female+Age',data=CigaretteConsumption_new).fit()
final_ml.params
final_ml.summary()
sales_pred=final_ml.predict(CigaretteConsumption_new)
import statsmodels.api as sm
sm.graphics.plot_partregress_grid(final_ml)
plt.scatter(CigaretteConsumption_new.Sales,sales_pred,c="r");plt.xlabel("Observed_values");plt.ylabel("Fitted_values")
plt.scatter(sales_pred,final_ml.resid_pearson,c="r"),plt.axhline(y=0,color="blue");plt.xlabel("Fitted_values")
plt.hist(final_ml.resid_pearson)
import pylab
import scipy.stats as st
st.probplot(final_ml.resid_pearson,dist="norm",plot=pylab)
plt.scatter(sales_pred,final_ml.resid_pearson,c="r"),plt.axhline(y=0,color="blue");plt.xlabel("Fitted_values");plt.ylabel("residuals")
from sklearn.model_selection import train_test_split
CigaretteConsumption_train,CigaretteConsumption_test=train_test_split(CigaretteConsumption_new,test_size=0.2)
model_train=smf.ols("Sales~Age+Female+HS",data=CigaretteConsumption_train).fit()
train_pred=model_train.predict(CigaretteConsumption_train)
train_resid =train_pred - CigaretteConsumption_train.Sales
train_rmse=np.sqrt(np.mean(train_resid*train_resid))
test_pred=model_train.predict(CigaretteConsumption_test)
test_resid=test_pred - CigaretteConsumption_test.Sales
test_rmse=np.sqrt(np.mean(test_resid*test_resid))
