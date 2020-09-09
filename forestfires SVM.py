# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:27:43 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
forestfires = pd.read_csv("C:\\Users\\Yogesh\\Downloads\\forestfires.csv")
forestfires.head()
def prep_model(hidden_dim):
    model = Sequential()
    for i in range(1,len(hidden_dim)-1):
        if (i==1):
            model.add(Dense(hidden_dim[i],input_dim=hidden_dim[0],Kernel_initializer="normal",activation="relu"))
        else:
            model.add(Dense(hidden_dim[i],activation="relu"))
            model.add(Dense(hidden_dim[-1]))
            model.compile(loss="mean_squared_error",optimizer="adam",metrics =["mse"])
            return (model)
column_names = list(forestfires.columns)
predictors = column_names[0:31]
target = column_names[31]
from keras.models import Sequential
from keras.layers import Dense
first_model = prep_model([31,50,1])
first_model.fit(np.arry(forestfires[predictors]),np.array(forestfires[target]),epochs=10)
pred_train = first_model.predict(np.array(forestfires[predictors]))
pred_train = pd.Series([i[0] for i in pred_train])
rmse_value = np.sqrt(np.mean((pred_train-forestfires[target])**2))
import matplotlib.pyplot as plt
plt.plot(pred_train,forestfires[target],"bo")
np.corrcoef(pred_train,forestfires[target])
