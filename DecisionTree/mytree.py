from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import graphviz
import pandas as pd
import json
import os


## dataset
wine = load_wine()
# print(wine.feature_names)
# print(wine.target_names)

feature_names = ['酒精',
                 '苹果酸',
                 '灰',
                 '灰的碱度',
                 '镁',
                 '总酚',
                 '类黄酮',
                 '非黄烷类酚类',
                 '花青素',
                 '颜色强度',
                 '色调',
                 'od280/od315稀释葡萄酒',
                 '脯氨酸']

## show in pandas
df = pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1)
# print(df.head())

Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
# print(Xtrain.shape)
# print(Xtest.shape)
# print(Ytrain.shape)
# print(Ytest.shape)

## 开始
clf0 = tree.DecisionTreeClassifier(criterion='entropy', random_state=None)  # random_state使得构建树时 不是所有的features都被使用，值任意
clf = clf0.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)  # 返回预测的准确度
# print(score)

# print(clf.tree_.children_left)
# print(clf.tree_.feature)
# print(clf.tree_.threshold)

# 把clf.tree_  持久化为json ???
# file = open("tree_dump.txt", mode="w", encoding="utf-8")
# json.dump(clf.tree_, file)
# file.close()

t = json.dumps(clf.tree_)
print(t)

# exit(0)

dot_data = tree.export_graphviz(clf
                                , out_file=None
                                , feature_names=wine.feature_names
                                , class_names=wine.target_names
                                , filled=True
                                , rounded=True
                                )

# graph = graphviz.Source(dot_data)
# graph.save("tree-save")
# graph.view("tree")

## 特征 的更多了解，哪些更重要呢？
# df = pd.concat([pd.DataFrame(clf.feature_importances_),
#                 pd.DataFrame(wine.feature_names)],
#                axis=1)
# print(df)

# print([*zip(wine.feature_names, clf.feature_importances_)])
