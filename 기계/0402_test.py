from sklearn.model_selection import train_test_split
import numpy as np

# 더미 데이터 생성
# X : 입력 값
# y : 출력 값값
X = np.random.rand(10, 2) * 5  # 1000개의 샘플, 10개의 특성
y = np.random.randint(0, 2, size=10)  # 0 또는 1의 이진 분류 라벨
print(X, y)
# # 80% 훈련 데이터, 20% 테스트 데이터 분할
X_train, X_test, y_train, y_test =\
    train_test_split(X, y, test_size=0.2, random_state=1)

print("훈련 데이터 크기:", X_train.shape)
print("테스트 데이터 크기:", y_test.shape)
