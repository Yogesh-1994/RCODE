# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:31:40 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
wc_at=pd.read_csv("C:\\Users\\Yogesh\\Desktop\\\wc_at.csv")
wc_at.columns
plt.hist(wc_at.Waist)
plt.boxplot(wc_at.Waist)
plt.plot(wc_at.Waist,wc_at.AT,"ro");plt.xlabel("Waist");plt.ylabel("AT")
wc_at.AT.corr(wc_at.Waist)
import statsmodels.formula.api as smf
model = smf.ols("AT~Waist", data=wc_at).fit()
model.summary()
print(model.conf_int(0.05))
pred = model.predict(wc_at.iloc[:,0])
plt.scatter(x = wc_at['Waist'],y = wc_at['AT'],color='red');plt.plot(wc_at['Waist'],pred,color='black');plt.xlabel('WAIST');plt.ylabel('TISSUE')
pred.corr(wc_at.AT)
model2 = smf.ols('AT~np.log(Waist)',data=wc_at).fit()
model2.params
model2.summary()
print(model.conf_int(0.05))
pred2 = model2.predict(pd.DataFrame(wc_at['Waist']))
pred2.corr(wc_at.AT)
pred2
plt.scatter(x=wc_at['Waist'],y = wc_at['AT'],color='green');plt.plot(wc_at['Waist'],pred,color='blue');plt.xlabel('WAIST');plt.ylabel('TISSUE')
model3 = smf.ols('np.log(AT)~Waist',data=wc_at).fit()
model3.params
model3.summary()
print(model.conf_int(0.01))
pred_log = model3.predict(pd.DataFrame(wc_at['Waist']))
pred_log
pred3 = np.exp(pred_log)
pred3
pred3.corr(wc_at.AT)
plt.scatter(x=wc_at['Waist'],y = wc_at['AT'],color='yellow');plt.plot(wc_at['Waist'],pred,color='green');plt.xlabel('WAIST');plt.ylabel('TISSUE')
