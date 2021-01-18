# 模型持久化

from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import os
from sklearn.externals import joblib

## dataset
wine = load_wine()

## split train/tmp3.json data
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

## rf-model
clf = tree.DecisionTreeClassifier(criterion='gini'
                                  , random_state=10
                                  , max_depth=3
                                  # , min_samples_leaf=10
                                  )

clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)
print(score)

## dump rf-model
# os.mkdir("model_save")
os.chdir("model_save")
joblib.dump(clf, "decision_tree_clf.m") # 持久化。但：如何持久化为json？ save rf-model as json



