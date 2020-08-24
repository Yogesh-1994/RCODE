# -*- coding: utf-8 -*-
"""Spyder Editorhis is a temporary script file.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Diabetes = pd.read_csv("C:\\Users\\Yogesh\\Downloads\\Diabetes.csv")
Diabetes.head()
Diabetes.columns
colnames=list(Diabetes.columns)
predictors=colnames[:8]
target=colnames[8]
x=Diabetes[predictors]
y=Diabetes[target]
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_jobs=2,oob_score=True,n_estimators=15,criterion="entropy")
np.shape(Diabetes)
rf.fit(x,y)
rf.estimators_
rf.n_classes_
rf.n_features_
rf.n_outputs_
rf.oob_score_
rf.predict(x)
Diabetes['rf_pred']=rf.predict(x)
cols= ['rf_pred',' class variable']
Diabetes[cols].head()
Diabetes[' class variable']
from sklearn.metrics import confusion_matrix
confusion_matrix(Diabetes[' class variable'],Diabetes['rf_pred'])
print("Accuracy",(498+266)/(498+266+2+2)*100)
Diabetes["rf_pred"]
