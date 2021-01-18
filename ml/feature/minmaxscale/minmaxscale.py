import numpy as np
import pandas as pd
import copy

min_bound = -2.
max_bound = 1.

data = pd.read_csv("data_null.csv")
fs = data.iloc[:, 1:5]

arr = np.array(fs)
print(arr)

mins = np.min(arr, 0)
maxs = np.max(arr, 0)
ranges = maxs - mins
dest = copy.deepcopy(arr)

print(mins, maxs, ranges)

for line in list(range(arr.shape[0])):
    for i in list(range(arr.shape[1])): # 遍历每一列
        if ranges[i] != 0.:
            dest[line, i] = (arr[line, i] - mins[i]) / ranges[i] * (max_bound - min_bound)  + min_bound
        else:
            dest[line, i] = 0.5 * (max_bound - min_bound) + min_bound

print("scaled data: ")
print(dest)


####  scale test data
print("========= scale test data ===========")
data_test = pd.read_csv("data_test.csv")
fs2 = data_test.iloc[:, 1:5]

arr_test = np.array(fs2)

dest_test = copy.deepcopy(arr_test)

for line in list(range(arr_test.shape[0])):
    for i in list(range(arr_test.shape[1])): # 遍历每一列
        if ranges[i] != 0.:
            dest_test[line, i] = (arr_test[line, i] - mins[i]) / ranges[i] * (max_bound - min_bound)  + min_bound
        else:
            dest_test[line, i] = 0.5 * (max_bound - min_bound) + min_bound

print("scaled test data: ")
print(dest_test)
