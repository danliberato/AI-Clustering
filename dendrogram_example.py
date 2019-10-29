import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering

#data = pd.read_csv('./datasets/100objs.csv')
data = pd.read_csv('./datasets/c2ds1-2sp.csv')

data = data.iloc[:, 1:3].values


plt.figure(figsize=(10, 7))
plt.title("Obj Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='single'))
plt.show()

'''cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='single')
cluster.fit_predict(data)

plt.figure(figsize=(10, 7))
print(data[:,1])
plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow')'''