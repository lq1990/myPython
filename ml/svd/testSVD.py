import numpy as np

A = np.array([[5,5,0,5],
                [5,0,3,4],
                [3,4,0,3],
                [0,0,5,3],
                [5,4,4,5],
                [5,4,5,5]
                ])  # (6,4)

U, Sigma0, VT = np.linalg.svd(A)
print(U)
print(Sigma0)
print(VT)

exit(0)

Sigma = np.zeros((6, 4))
for i in list(range(len(Sigma0))):
    Sigma[i, i] = Sigma0[i]
#

# print(U.dot(Sigma).dot(VT))

a1 = np.array([[5,4,3,3,5,5]]).T
print(a1)

K = 2
v1 = a1.T.dot(U[:, 0:K]).dot(np.linalg.inv(Sigma[0:K, 0:K]))

print(v1)