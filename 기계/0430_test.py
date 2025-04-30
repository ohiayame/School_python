from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()

X = data.data
y = data.target
feature_message = data.feature_names

print(type(data), type(X), type(feature_message))


print("입력 X shape: ", X.shape)
print("타겟 y shape: ",y.shape)
print("특성 이름: ", feature_message)
print("설명: ", data.DESCR[:1000])