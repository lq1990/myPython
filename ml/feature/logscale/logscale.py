import numpy as np
import pandas as pd
import copy


data = pd.read_csv("logscale_data.csv")
fs = data.iloc[:, 1:5]

arr = np.array(fs)
print("arr: \n",arr)

mins0 = np.min(arr, 0)
maxs0 = np.max(arr, 0)

shifts = 1. - mins0
maxs = maxs0 + shifts
logmaxs = np.log10(maxs)

print("shift: ",shifts)
print("maxs: ", maxs)
print("logmaxs:", logmaxs)

# logscale, log10(val) / log10(max(val))
scaled = np.log10(arr + shifts) / logmaxs
print("scaled: \n", scaled)

print("================")
print("================")
print("================")
#==========================================================
#==========================================================
#==========================================================
# test data
data_test = pd.read_csv("logscale_data_test.csv")
fs_test = data_test.iloc[:, 1:5]
arr_test = np.array(fs_test)

arr_test_shifts = arr_test + shifts
print("arr_test_shifts: ",arr_test_shifts)

## pre_process arr_test
for i in list(range(arr_test_shifts.shape[0])):
    for j in list(range(arr_test_shifts.shape[1])):
        arr_test_shifts[i, j] = max(arr_test_shifts[i,j], 1.)  # 限制testdata的最小值为1. 因为小于1的话，log函数会急剧变化。
        # 不限制最大值。


print("arr_test_shifts2: ",arr_test_shifts)

scaled_test = np.log10(arr_test_shifts) / logmaxs
print("scaled_test: \n", scaled_test)

