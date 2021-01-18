import sklearn_json as skljson
import pandas as pd
from sklearn import linear_model
import numpy as np


# load csv
boston_train = pd.read_csv("data/boston_train_with_label.csv", encoding="utf-8")
boston_test = pd.read_csv("data/boston_test_with_label.csv", encoding="utf-8")

Xtrain = boston_train.iloc[:, 0:boston_train.shape[1]-1]
Ytrain = boston_train.iloc[:, boston_train.shape[1]-1]

Xtest = boston_test.iloc[:, 0:boston_test.shape[1]-1]
Ytest = boston_test.iloc[:, boston_test.shape[1]-1]

# print(Xtrain.head()); print(Xtrain.shape)
# print(Ytrain.head()); print(Ytrain.shape)


# train linearreg
reg = linear_model.LinearRegression()
reg = reg.fit(Xtrain, Ytrain) # model is reg

# predict
pred = reg.predict(Xtest)
vs = pd.concat([
    pd.DataFrame(np.array(Ytest).reshape(pred.shape[0],1), columns=["label"]),
    pd.DataFrame(pred.reshape(pred.shape[0],1), columns=["pred"])
    ], axis=1)
print(vs)


# save model to json
# skljson.to_json(reg, "json/linearreg_for_boston_from_skljson.json")


