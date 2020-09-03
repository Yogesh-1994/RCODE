# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:45:24 2020

@author: Yogesh
"""


import pandas as pd
Company_Data = pd.read_csv("C:\\Users\\Yogesh\\Downloads\\Company_Data.csv")
Company_Data .head()
Company_Data ['Urban'].unique()
Company_Data .Urban.value_counts()
colnames=list(Company_Data .columns)
predictors=colnames[:5]
target=colnames[5]
import numpy as np
from sklearn.model_selection import train_test_split
train,test=train_test_split(Company_Data ,test_size=0.2)
from sklearn.tree import DecisionTreeClassifier
help(DecisionTreeClassifier)
model=DecisionTreeClassifier(criterion="entropy")
model.fit(train[predictors],train[target])
preds=model.predict(test[predictors])
pd.Series(preds).value_counts()
pd.crosstab(test[target],preds)
np.mean(preds==test.Urban)   
