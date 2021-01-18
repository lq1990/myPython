# sklearn rf-model, serialize as json

import sklearn_json as skljson
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

## load data
wine = load_wine()

## split train/tmp3.json
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

model = RandomForestClassifier(n_estimators=10, max_depth=5, random_state=0)\
    .fit(Xtrain, Ytrain)

## to json
skljson.to_json(model, "rf-model")

## from_json
model2 = skljson.from_json("rf-model")
score = model2.score(Xtest, Ytest)
print(score)


