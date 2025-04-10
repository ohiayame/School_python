import numpy as np

# H(x) = 5X + 3X + 3
num_of_sample = 5
num_of_features = 2

# data set 
np.random.seed(1)
np.set_printoptions(False, suppress=True)
X = np.random.rand(num_of_sample, num_of_features) * 10

x_true = [5, 3]
b_true = 4
noise = np.random.randn(num_of_sample) * 0.5

# 가설 = (특성 1 * 1의 W) + (특성 2 * 2의 W) + 바이어스
y = X[:, 0] * 5 + X[:, 1] * 3 + b_true + noise

print(X)
print(X[:, 0]) # 모든 샘플의 첫번째 특성 모두 
print(X[:, 0] * 5)
print(X[:, 1]) # 모든 샘플의 두번째 특성 모두 
print(X[:, 1] * 3)

print(X[:, 0] * 5 + X[:, 1] * 3 + b_true)  # H(X)
