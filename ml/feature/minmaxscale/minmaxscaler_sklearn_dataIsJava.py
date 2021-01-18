import numpy as np
from sklearn.preprocessing import MinMaxScaler

minBound = -1.
maxBound = 0.5
scale = maxBound - minBound

train_data = np.array([[-5.1, 1.2, 0, 200.1],
                       [-2.0, 1.2, 0, 3],
                       [1.2, 1.2, 0, -1.5],
                       [2.7, 1.2, 0, 0.5]])

train_data_null = np.array([[-5.1, 1.2, 0, 200.1],
                       [-2.0, 0., 0, 3],
                       [1.2, 0., 0, -1.5],
                       [2.7, 0., 0, 0.5]])

test_data = np.array([[-15.1, 0, 1, 1],
                      [-1.0, 1.2, 1, 6],
                      [0.2, 1.2, 1, 1.5],
                      [2.6, 1.2, 1, -0.5]])

scaler = MinMaxScaler((minBound, maxBound))
scaler.fit(train_data)

print("scaled train data:\n",scaler.transform(train_data))

print("scaled test data: \n", scaler.transform(test_data))


