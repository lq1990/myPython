import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer

data = pd.read_csv("logscale_data.csv")
fs = data.iloc[:, 1:5]
arr = np.array(fs)
print("arr: \n", arr)

mins0 = np.min(arr, 0)
maxs0 = np.max(arr, 0)
shifts = 1. - mins0
arr_shifts = arr+shifts
print("arr_shift:\n", arr_shifts)

# create transformer
transformer = FunctionTransformer(np.log1p)
res = transformer.transform(arr_shifts)
print("---\nlog10 scaled: \n", res)
