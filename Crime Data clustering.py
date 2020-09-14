# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:10:28 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
X=np.random.uniform(0,1,1000)
Y=np.random.uniform(0,1,1000)
df_XY=pd.DataFrame(columns=["X","Y"])
df_XY.X=X
df_XY.Y=Y
df_XY.plot(x="X",y="Y", kind="scatter")
model1=KMeans(n_clusters=5).fit(df_XY)
df_XY.plot(x="X",y="Y", c=model1.labels_, kind="scatter",s=10,cmap=plt.cm.coolwarm)
crime_data= pd.read_csv("C:\\Users\\Yogesh\\Downloads\\crime_data.csv")
def norm_func(i):
    x=(i - i.min())/(i.max() - i.min())
    return(x)
df_norm=norm_func(crime_data.iloc[:,1:])
df_norm.head(10)
k=list(range(2,23))
k
TWSS= []
for i in k:
    kmeans= KMeans(n_clusters =i)
    kmeans.fit(df_norm)
    WSS= []
    for j in range(i):
        WSS.append(sum(cdist(df_norm.iloc[kmeans.labels_==j,:], kmeans.cluster_centers_[j].reshape(1,df_norm.shape[1]),"euclidean")))
        TWSS.append(sum(WSS))
plt.plot(k,TWSS,'ro-');plt.xlabel("No_of_clusters");plt.ylabel("Total_within_ss");plt.xticks(k)
model= KMeans(n_clusters=5)
model.fit(df_norm)
model.labels_
md= pd.Series(model.labels_)
crime_data['clust']=md
df_norm.head()
crime_data.iloc[:1,:7].groupby(crime_data.clust).mean()
