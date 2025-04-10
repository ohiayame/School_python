from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
np.set_printoptions(suppress=True, precision=1)
# bar = np.zeros((2)) # 원소가 2개인 1차원 배열
# foo = np.zeros((3,5)) # 원소가 한 배열에 2개인 2차원배열 (배열 -> 3개)
# pos = np.zeros((2, 3, 2)) # 원소가 한 배열에 2개인 3차원 배열(배열 3개 -> 2개)

X = np.random.rand(100, 1)* 10
print(X)
# for문을 안돌려도 모든 값에 5가 곱해짐
# y = 2.5 * X + np.random.randn(3, 1) * 2
# y = y.ravel()

# # model생성 후 하이퍼파라미터 설정
# model = SGDRegressor(
#     max_iter=100,
#     learning_rate='constant',
#     eta0=0.001, # 학습률
#     penalty=None, # 정규화 제거
#     random_state=0 # 결과 재현을 위한 시드 고정
# )

# # 학습 실시
# model.fit(X, y)

# # 평가
# # Loss
# y_pred = model.predict(X)

# mse = mean_squared_error(y, y_pred)