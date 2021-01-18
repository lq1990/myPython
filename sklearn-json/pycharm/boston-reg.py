import sklearn_json as skljson
from sklearn.datasets import load_boston   # for regression use
from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn_json
from sklearn.datasets import load_boston   # for regression use
from sklearn import linear_model
import pandas as pd

# dataset
boston = load_boston()
# print(boston.data.shape)
# print(boston.feature_names)
# print(boston.target, boston.target.shape)

# train/tmp3.json split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(boston.data, boston.target, test_size=0.3)

# pandas
boston_train_with_label = pd.concat([pd.DataFrame(Xtrain, columns=boston.feature_names), pd.DataFrame(Ytrain, columns=['label'])], axis=1)
boston_test_with_label = pd.concat([pd.DataFrame(Xtest, columns=boston.feature_names), pd.DataFrame(Ytest, columns=['label'])], axis=1)

# data = pd.concat([pd.DataFrame(boston.data, columns=boston.feature_names),
#                   pd.DataFrame(boston.target, columns=["PRICE"])],
#                  axis=1)
# print(data.head())

boston_train_with_label.to_csv("boston_train_with_label2.csv", encoding="utf-8", index=False)
boston_test_with_label.to_csv("boston_test_with_label2.csv", encoding="utf-8", index=False)
data = pd.concat([pd.DataFrame(boston.data, columns=boston.feature_names),
                  pd.DataFrame(boston.target, columns=["PRICE"])],
                 axis=1)

print(data.head())

# to csv
# data.to_csv("./boston.csv", encoding="utf-8", mode="w", header=True, index=False)



# model
# skljson.to_json(clf, "tree_model")

