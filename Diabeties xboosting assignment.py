# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:10:27 2020

@author: Yogesh
"""


import xgboost as xgb
import pandas as pd
Diabetes = pd.read_csv("C:\\Users\\Yogesh\\Downloads\\Diabetes.csv")
Diabetes.head(10)
Diabetes.isnull().sum()
from sklearn.model_selection import train_test_split
X,y=Diabetes.iloc[:,:8],Diabetes.iloc[:,8]
train_x,test_x,train_y,test_y=train_test_split(X,y,test_size=0.28,random_state=10)
xgb1=xgb.XGBClassifier(n_estimators=2000,learning_rate=0.3)
xgb1.fit(train_x,train_y)
train_pred=xgb1.predict(train_x)
import numpy as np
train_acc=np.mean(train_pred==train_y)
train_acc
test_pred=xgb1.predict(test_x)
test_acc=np.mean(test_pred==test_y)
test_acc
from xgboost import plot_importance
plot_importance(xgb1)
