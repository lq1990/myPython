# load rf-model and use it
from sklearn.externals import joblib
from sklearn.datasets import load_wine

wine = load_wine()

clf = joblib.load("model_save/decision_tree_clf.m")
score = clf.score(wine.data, wine.target)
print(score)

