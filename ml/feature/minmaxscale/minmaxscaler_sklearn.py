import numpy as np
from sklearn.preprocessing import MinMaxScaler

minBound = 0.
maxBound = 1.
scale = maxBound - minBound

train_data = np.array([[1, 2, 10], # take 1, scaled val: (1-min=1)*(scale=5) +(minBound=-3) = -3.    take 2, scaled val: (2-2)*5 - 3 = -3,    take 10, scaled val: (10-min=0.5)/(range=9.5)*(scale=5)-3 = 2
                       [1, 2, 1],
                       [1, 2, 0.5]]) # if min=max, set val=minBound

test_data = np.array([[11, 10, 0], # take 11, scaled val: (11-min=1)/(range=0)*(scale=5)+(minBound=-3) = 47.
                      # take 10, scaled val: (10-min=2)/range=0*(scale=5)-3 = 37.
                      # take 0, scaled val: (0-min=0.5)/(range=9.5)*(scale=5)+(minBound=-3) = -3.263
                      [10, 5,  1],
                      # take 10, val=(10-1)/0*5-3 = 42   直接不除以0了，继续往下计算
                      # take 1, val=(1-0.5)/9.5*5-3 = -2.736
                      [1,  0,  0.5]])

scaler = MinMaxScaler((minBound, maxBound))
scaler.fit(train_data)

print("scaled train data:\n",scaler.transform(train_data))

print("scaled test data: \n", scaler.transform(test_data))


