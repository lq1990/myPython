from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd


# datasets
wine = load_wine()

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
print(Xtrain.shape)
print(Xtest.shape)
print(Ytrain.shape)
print(Ytest.shape)


# pd
# wine_train_with_label = pd.concat([pd.DataFrame(Xtrain, columns=wine.feature_names), pd.DataFrame(Ytrain, columns=['label'])], axis=1)
# wine_test_with_label = pd.concat([pd.DataFrame(Xtest, columns=wine.feature_names), pd.DataFrame(Ytest, columns=['label'])], axis=1)
wine_test_no_label = pd.DataFrame(Xtest, columns=wine.feature_names)


# wine_train_with_label.to_csv("wine_train_with_label.csv", encoding="utf-8", index=False)
# wine_test_with_label.to_csv("wine_test_with_label.csv", encoding="utf-8", index=False)
wine_test_no_label.to_csv("wine_test_no_label.csv", encoding="utf-8", index=False)

