import numpy as np
from time  import time

loops = 1000
nrows = 1000
ncols = 1000

arr = np.random.rand(nrows, ncols)

begin = time()
for i in list(range(loops)):
    np.mean(arr, 0)

end = time()
print("dtime", (end-begin))

