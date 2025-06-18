from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터셋 로딩 및 분할
digits = load_digits()
features = digits.data       # (1797, 64): 8x8 이미지 벡터
labels = digits.target       # (1797,): 0~9 클래스 정수

# print(features.shape)
# print(labels.shape)
# print(labels[:30])

# 2. 학습/테스트 셋 분할
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42, stratify=labels
)

# 3. 표준화 (평균 0, 분산 1)
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

np.set_printoptions(suppress=True)

num_features = X_train_std.shape[1]  # 64
num_samples = X_train_std.shape[0]   # 1437
num_classes = 10
learning_rate = 0.1

W = np.random.randn(num_features, num_classes)  # 64, 10
b = np.zeros(num_classes)
epoch = 10000

for i in range(epoch):
    # logits -> softmax (확률) -> 지수 
    # 각 클래스의 로짓을 계산 /  X(1437, 64) @ W(64, 10) + b(10,)
    logit = X_train_std @ W  + b # 1437, 10
    logit_max = np.max(logit, axis=1, keepdims=True)
    logit -= logit_max

    exp_logit = np.exp(logit)
    exp_logit_sum = np.sum(exp_logit, axis=1, keepdims=True)

    softmax = exp_logit / exp_logit_sum

    i_matix = np.eye(num_classes)
    one_hot = i_matix[y_train]   # 1437, 10

    # error  softmax(1437, 10) - one_hot(1437, 10)
    error = softmax - one_hot

    gradient_w = X_train_std.T @ error / num_samples
    gradient_b = np.sum(error, axis=0) / num_samples


    # update
    W -= learning_rate * gradient_w
    b -= learning_rate * gradient_b

    # loss
    loss = -np.sum(np.log(softmax + 1e-15) * one_hot) / num_samples
    if epoch % 1000 == 0:
            print(f"Train Loss: {loss:.4f}")


def predict(arg_X, arg_label):
    # logits -> softmax (확률) -> 지수 
    # 각 클래스의 로짓을 계산 /  X(1437, 64) @ W(64, 10) + b(10,)
    logit = arg_X @ W  # 1437, 10
    logit_max = np.max(logit, keepdims=True)
    logit -= logit_max

    exp_logit = np.exp(logit)
    exp_logit_sum = np.sum(exp_logit, keepdims=True)

    softmax = exp_logit / exp_logit_sum
    predict = np.argmax(softmax)
    print(f"label: {arg_label}, predict: {predict}")
    
for idx in range(10):
    predict(X_test_std[idx], y_test[idx])