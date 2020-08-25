# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 21:08:16 2020

@author: Yogesh
"""


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
Universities = pd.read_csv("C:\\Users\\Yogesh\\Downloads\\Universities.csv")
def norm_func(i):
    X=(i-i.min())/  (i.max() - i.min())
    return(X)
df_norm=norm_func(Universities.iloc[:,1:])
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
type(df_norm)
z= linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15, 5));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(
    z,
    leaf_rotation=0.,
    leaf_font_size=8.,
    )
plt.show()
help(linkage)
from sklearn.cluster import AgglomerativeClustering
h_complete =AgglomerativeClustering(n_clusters=3, linkage='complete', affinity="euclidean").fit(df_norm)
cluster_labels= pd.Series(h_complete.labels_)
Universities['clust']=cluster_labels
Universities= Universities.iloc[:,[7,0,1,2,3,4,5,6]]
Universities.head()
Universities.iloc[:,2:].groupby(Universities.clust).mean()
Universities.to_csv("Uni.csv",encoding="utf-8")
import os
os.getcwd()
os.chdir('D:\\Session')
