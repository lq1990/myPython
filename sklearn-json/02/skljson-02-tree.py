# save model to json

from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import sklearn_json as skljson
import graphviz

# data
wine = load_wine()

# train/tmp3.json split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

# train with deicision tree
clf = tree.DecisionTreeClassifier(criterion='gini'
                                  # , max_depth=5
                                  , random_state=None
                                  # , min_samples_leaf=5
                                  )
clf = clf.fit(Xtrain, Ytrain)

print("train accu: "+str(clf.score(Xtrain, Ytrain)))
print("tmp3.json  accu: "+str(clf.score(Xtest, Ytest)))

# show
dot_data = tree.export_graphviz(clf
                                , out_file=None
                                , feature_names=wine.feature_names
                                , class_names=wine.target_names
                                , filled=True
                                , rounded=True
                                )

graph = graphviz.Source(dot_data)
graph.view("tree")

# model to json
skljson.to_json(clf, "tree_model")

# ===============================================
# ===============================================
# ===============================================




