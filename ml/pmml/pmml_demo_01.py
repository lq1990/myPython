'''
PMML: Predictive Model Markup Language
使用PMML作为跨平台的数据格式。比如在python sklearn <=> Spark

考虑到数据预处理-训练的过程，可以使用Pipeline对全流程持久化下来。
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml
import os

os.environ['PATH'] += os.pathsep + 'F:/Program Files/Java/jdk1.8.0_221/bin'

X = [[1, 2, 3, 1], [2, 4, 1, 5], [7, 8, 3, 6], [4, 8, 4, 7], [2, 5, 6, 9]]
y = [0, 1, 0, 2, 1]

pipeline = PMMLPipeline([("classifier", tree.DecisionTreeClassifier(random_state=0))])
pipeline.fit(X, y)

sklearn2pmml(pipeline, ".\demo01.pmml", with_repr=True)

