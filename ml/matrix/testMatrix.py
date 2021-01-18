import numpy as np

arr = np.array([[1,2,3,4,5,6]])
arr_C = np.reshape(arr,(3,2), order="C") # default, C-like, row-major
arr_F = np.reshape(arr,(3,2), order="F") # Fortran-like, col-major

print(arr)
# [[1 2 3 4 5 6]]

print(arr_C) # row-major
# [[1 2]
#  [3 4]
#  [5 6]]

print(arr_F)
# [[1 4]
#  [2 5]
#  [3 6]]
