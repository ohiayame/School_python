import numpy as np

# h(x) = wx1 + wx2 + wx3 + b
num_of_features = 3
num_of_sample = 2

np.random.seed(1)
np.set_printoptions(suppress=True, precision=3)
X = np.random.rand(num_of_sample, num_of_features)


w_true = np.random.randint(1, 10, num_of_features)
b_true = np.random.randn() * 0.5

# 가설 = (특성 1 * 1의 W) + (특성 2 * 2의 W) + 바이어스
# X[:, 0] * w_true[0] + 
# X[:, 1] * w_true[1] + 
# X[:, 2] * w_true[2] + b_true

y = X @ w_true + b_true

w = np.random.rand(num_of_features)
b = np.random.randn()
gradient = np.zeros(num_of_features)
learning_rate = 0.1
epochs = 1000
# print(w, b)


for epoch in range(epochs):
    # prediction 예측 값
    prediction = X @ w + b
    # print(pridiction)
    # error
    error = prediction - y
    # print(error)
    # print(X.T)

    gradient_w = X.T @ error / num_of_features

    # print(gradient_w)

    w -= learning_rate * gradient_w
    b -= learning_rate * error.mean()
    # print(w, b)

print(f"w_true: {w_true}, b_true: {b_true}")
print(f"w: {w.round(3)}, b: {round(b, 3)}")