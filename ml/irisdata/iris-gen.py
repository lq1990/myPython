import numpy as np
from sklearn.datasets import load_iris

data = load_iris()['data']
target = load_iris()['target']

print(data)
print(target)



exit(0)

x_data = np.hstack((target.reshape(-1, 1), data))
x_data = x_data[x_data[:, 0] <= 1]

train_index = [i for i in np.random.randint(0, len(x_data), int(len(x_data) * 0.8))]
test_index = list(set([i for i in range(len(x_data))]) - set(train_index))

train = x_data[train_index]
test = x_data[test_index]

with open("iris_train.txt", "w") as f:
    for line in train:
        f.write(",".join([str(x) for x in line]) + "\n")

with open("iris_test.txt", "w") as f:
    for line in test:
        f.write(",".join([str(x) for x in line]) + "\n")
