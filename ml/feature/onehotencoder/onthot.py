import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


data = pd.read_csv("onehot_data.csv")
fs = data.iloc[:, 1:2]

arr = np.array(fs)
print("arr original: ",arr)


# fit
onehot = OneHotEncoder(categories=[['apple', 'banana', 'pear']], drop='first')
onehot.fit(arr)
print("categories_: ", onehot.categories_)
print(onehot.transform(arr).toarray())

## 问题： 不能对arr 自动对其中的某些列进行onehot。
## 而得手动先提取列出来

