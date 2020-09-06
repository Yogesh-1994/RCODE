# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:05:26 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
glass = pd.read_csv("C:\\Users\\Yogesh\\Downloads\\glass.csv")
from sklearn.model_selection import train_test_split
train,test = train_test_split(glass,test_size=0.2)
from sklearn.neighbors import KNeighborsClassifier as KNC
neigh = KNC(n_neighbors=3)
neigh.fit(train.iloc[:,0:9],train.iloc[:,9])
train_acc = np.mean(neigh.predict(train.iloc[:,0:9])==train.iloc[:,9])
test_acc = np.mean(neigh.predict(test.iloc[:,0:9])==test.iloc[:,9])
neigh = KNC(n_neighbors=5) 
neigh.fit(train.iloc[:,0:9],train.iloc[:,9])
train_acc = np.mean(neigh.predict(train.iloc[:,0:9])==train.iloc[:,9])
test_acc = np.mean(neigh.predict(test.iloc[:,0:9])==test.iloc[:,9])                                                         
neigh = KNC(n_neighbors=1)
neigh.fit(train.iloc[:,0:9],train.iloc[:,9])
train_acc = np.mean(neigh.predict(train.iloc[:,0:9])==train.iloc[:,9])
test_acc = np.mean(neigh.predict(test.iloc[:,0:9])==test.iloc[:,9])
acc = []
for i in range(9,50,2):
    neigh = KNC(n_neighbors=i)
    neigh.fit(train.iloc[:,0:9],train.iloc[:,9])
    train_acc
    test_acc
    acc.append([train_acc,test_acc])
import matplotlib.pyplot as plt
plt.plot(np.arange(9,50,2),[i[0]for i in acc],"ro-")
plt.plot(np.arange(9,50,2),[i[1]for i in acc],"bo-")
