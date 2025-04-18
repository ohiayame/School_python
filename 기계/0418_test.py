import numpy as np
num_features = 4
num_samples = 10000

np.random.seed(5)

X = np.random.rand(num_samples, num_features) * 2
w_true = np.random.randint(1, 11, (num_features, 1))
b_true = np.random.randn() * 0.5

y = X @ w_true + b_true

w = np.random.rand(num_features, 1)
b = np.random.rand()
learning_rate = 0.01
gradient = np.zeros(num_features)

for _ in range(10000):
    # 예측값
    predict_y = X @ w + b

    # 오차  
    error = predict_y - y

    # 기울기 
    gradient_w = X.T @ error / num_samples
    gradient_b = error.mean()

    # 업데이트
    w -= learning_rate * gradient_w
    b -= learning_rate * gradient_b

print(f"W_true : {w_true},\n b_true: {b_true}\n")
print(f"W : {w},\n b: {b}\n")