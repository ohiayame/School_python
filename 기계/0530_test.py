import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pylab as plt


# x = np.arange(10)

# print(x.mean(), x.std())

# mean = x.mean()
# values = [item - mean for item in x]
# print(values)


# x = np.arange(1, 11)

# max = x.max()
# min = x.min()

# values = [(item - min) / (max - min) for item in x]
# print(values)

one_hot = np.eye(4)
print(one_hot, "\n\n")

y_li = [0, 1, 0, 3, 2, 3]
one_hot_value = one_hot[y_li]
print(one_hot_value)
print(np.argmax(one_hot_value, axis=0))