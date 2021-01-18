# read and save model in file

import json
import sklearn_json as skljson
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine

f = json.load(open("tree_model", mode='r', encoding='utf-8'))
# print(f, type(f))
# print(f['meta'])

# ======================================
# 读取json文件的model，使用model
# ======================================
wine = load_wine()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

model = skljson.from_json("tree_model")

print(model.score(Xtrain, Ytrain))
print(model.score(Xtest, Ytest))

print(model.predict(Xtest))
print(Ytest)

