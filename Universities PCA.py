# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:08:33 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
Universities = pd.read_csv("C:\\Users\\Yogesh\\Downloads\\Universities.csv")
Universities.describe()
Universities.head()
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
Universities.data = Universities.iloc[:,1:]
Universities.data.head() 
UNI = Universities.data.values
UNI
Universities_normal = scale(UNI)
pca = PCA(n_components=6)
pca_values=pca.fit_transform(Universities_normal)
var= pca.explained_variance_ratio_
var
pca.components_[0]
var1 = np.cumsum(np.round(var,decimals=4)*100)
var1
plt.plot(var1, color="blue")
