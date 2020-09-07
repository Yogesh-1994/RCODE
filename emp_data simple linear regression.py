# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:31:40 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
emp_data = pd.read_csv("C:\\Users\\Yogesh\\Downloads\\\emp_data.csv")
emp_data.columns
plt.hist(emp_data.Salary_hike)
plt.boxplot(emp_data.Salary_hike)
plt.plot(emp_data.Salary_hike,emp_data.Churn_out_rate,"ro");plt.xlabel("Salary_hike");plt.ylabel("Churn_out_rate")
emp_data.Churn_out_rate.corr(emp_data.Salary_hike)
import statsmodels.formula.api as smf
model = smf.ols("Churn_out_rate~Salary_hike", data=emp_data).fit()
model.summary()
print(model.conf_int(0.05))
pred = model.predict(emp_data.iloc[:,0])
plt.scatter(x = emp_data['Salary_hike'],y = emp_data['Churn_out_rate'],color='red');plt.plot(emp_data['Salary_hike'],pred,color='black');plt.xlabel('SALARY HIKE');plt.ylabel('CHURN OUT RATE')
pred.corr(emp_data.Churn_out_rate)
model2 = smf.ols('Churn_out_rate~np.log(Salary_hike)',data=emp_data).fit()
model2.params
model2.summary()
print(model.conf_int(0.05))
pred2 = model2.predict(pd.DataFrame(emp_data['Salary_hike']))
pred2.corr(emp_data.Churn_out_rate)
pred2
plt.scatter(x=emp_data['Salary_hike'],y = emp_data['Churn_out_rate'],color='green');plt.plot(emp_data['Salary_hike'],pred,color='blue');plt.xlabel('SALARY HIKE');plt.ylabel('CHURN OUT RATE')
model3 = smf.ols('np.log(Churn_out_rate)~Salary_hike',data=emp_data).fit()
model3.params
model3.summary()
print(model.conf_int(0.01))
pred_log = model3.predict(pd.DataFrame(emp_data['Salary_hike']))
pred_log
pred3 = np.exp(pred_log)
pred3
pred3.corr(emp_data.Churn_out_rate)
plt.scatter(x=emp_data['Salary_hike'],y = emp_data['Churn_out_rate'],color='yellow');plt.plot(emp_data['Salary_hike'],pred,color='green');plt.xlabel('SALARY HIKE');plt.ylabel('CHURN OUT RATE')
