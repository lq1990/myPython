# java中的PCATest用到的数据集: pca_data.csv

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

k = 4

data = pd.read_csv("pca_data.csv")
fs = data.iloc[:, 1:5]

features = np.array(fs)

# standardscale
scaledFeatures = (features - np.mean(features, 0)) / np.std(features, 0, ddof=1)
print("src: ")
print(scaledFeatures)

## my pca
ew, ev = np.linalg.eig(np.cov(scaledFeatures.T))
ew_order = np.argsort(ew)[::-1]
ew_sort = ew[ew_order]; print("ew: ", ew_sort)
ev_sort = ev[:,ew_order]
# V
V = ev_sort[:,:k]
print("V: ", V)
print(np.sqrt(np.sum(V*V)))  # mod = 1
# Xnew
X_new = scaledFeatures.dot(V)
print("my")
print(X_new)

# print(np.matmul(X_new[:,0].T, X_new[:, 1])) # 0
# print(np.matmul(X_new[:,0].T, X_new[:, 2])) # 0
# print(np.matmul(X_new[:,1].T, X_new[:, 2])) # 0

## use PCA
pca = PCA(n_components=k, whiten=False)  # , whiten=True
data_pca = pca.fit_transform(scaledFeatures)
print("use PCA: ")
print(data_pca)
print(np.matmul(data_pca[:,0].T, data_pca[:, 1])) # 0

exit(0)

#####################
"[-2.1648953015,-0.2448571929]"
"[-0.0411093863,-0.4278952371]"
"[-0.1392078688,0.1080710094]"
"[0.7776332235,1.7948303938]"
"[1.5675793331,-1.2301489732]"

arr = np.array([[-2.1648953015, -0.0411093863, -0.1392078688, 0.7776332235, 1.5675793331],[-0.2448571929, -0.4278952371, 0.1080710094, 1.7948303938, -1.2301489732] ]).T
print("from spark: ")
print(arr)

arr1 = arr[:,0]
arr2 = arr[:,1]
print("matmul: ")
print(np.matmul(arr[:,0], arr[:,1]))

print("arr1: ")
print(np.mean(arr1))
print(np.std(arr1))
print(np.std(arr1, ddof=1))

print("arr2: ")
print(np.mean(arr2))
print(np.std(arr2))
print(np.std(arr2, ddof=1))