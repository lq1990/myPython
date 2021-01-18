import numpy as np
from time  import time

loops = 10000
nrows = 100
ncols = 100

mat = np.random.rand(nrows, ncols)
vec = np.random.rand(ncols, 1)

begin = time()
for i in list(range(loops)):
    res = mat.dot(vec)

end = time()
print("dtime", (end - begin)*1000)

# print(res)