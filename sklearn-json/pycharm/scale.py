'''
standard scale
for diy.csv
'''

import pandas as pd
import numpy as np


def standardscale ():
    return


file = pd.read_csv("./data/wine_train_with_label_diy.csv")
print(file.head())
print(file.describe())

file.describe().to_csv("./data/wine_diy_desc.csv")
