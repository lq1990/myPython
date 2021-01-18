import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")
# print(data)

f1 = np.array(data.iloc[:, 0])
fir1_f1 = np.array(data.iloc[:, 3])


plt.subplot(2, 1, 1)
plt.plot(f1)
plt.grid()
plt.title("f1")

plt.subplot(2, 1, 2)
plt.plot(fir1_f1)
plt.grid()
plt.title("fir1 f1")

plt.show()
