# 1. 필수 라이브러리 불러오기
import numpy as np
from sklearn.datasets import fetch_california_housing    # 캘리포니아 주택 데이터셋
from sklearn.linear_model import SGDRegressor             # 확률적 경사하강법 회귀 모델
from sklearn.model_selection import train_test_split      # 훈련/테스트 데이터 분할 함수
from sklearn.preprocessing import StandardScaler          # 특성 정규화를 위한 스케일러
from sklearn.metrics import mean_squared_error, r2_score  # 성능 평가 지표
import matplotlib.pyplot as plt                           # 시각화를 위한 라이브러리

# 2. 데이터 로딩
# fetch_california_housing() 함수로 입력 데이터(X)와 타깃값(y)을 불러옴
data = fetch_california_housing()
X = data.data                        # 입력 특성 (8개 컬럼)
y = data.target                      # 타겟 변수 (중간 주택 가격, 단위: $100,000)
feature_names = data.feature_names  # 특성 이름 목록

# 3. 학습용/테스트용 데이터 분할 (훈련: 80%, 테스트: 20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. 입력 특성 정규화 (표준화: 평균 0, 표준편차 1로 맞춤)
# SGD는 입력값 크기에 민감하므로 반드시 정규화가 필요
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # 훈련 데이터를 기준으로 스케일 조정
X_test_scaled = scaler.transform(X_test)         # 동일한 기준으로 테스트 데이터 변환

# 5. SGDRegressor 모델 정의 및 학습
model = SGDRegressor(
    max_iter=10000,            # 최대 반복 횟수 (epoch 수)
    tol=0.0007,                 # 손실이 tol보다 작아지면 학습 중단 (수렴 기준)
    eta0=0.001,               # 학습률 초기값
    learning_rate='invscaling',# 학습률 고정 방식
    penalty=None,             # 정규화 없음 (과적합 방지 설정 사용 안함)
    random_state=42           # 결과 재현을 위한 시드 고정
)
model.fit(X_train_scaled, y_train)  # 학습 수행

# 6. 예측 및 평가
y_pred = model.predict(X_test_scaled)  # 테스트 데이터 예측 수행

# MSE (평균제곱오차), R² (설명력 지표) 출력
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"R² score: {r2_score(y_test, y_pred):.4f}")

# 회귀 계수 출력 (각 특성이 결과에 얼마나 영향을 주는지 보여줌)
print("\n회귀 계수 (weights):")
for name, coef in zip(feature_names, model.coef_):
    print(f"{name:<20}: {coef:>20.2f}")

# 절편(bias term) 출력
print(f"\n절편 (bias): {model.intercept_[0]:.2f}")

# 예측 결과 시각화 (실제값 vs 예측값 산점도)
plt.scatter(y_test, y_pred, alpha=0.3)  # 예측 분포를 산점도로 표현
plt.xlabel("Actual Median House Value")  # 실제 집값
plt.ylabel("Predicted Value")            # 예측된 집값
plt.title("SGDRegressor Prediction vs Actual")  # 그래프 제목
plt.grid(True)  # 격자 표시
plt.show()
