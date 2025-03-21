import numpy as np
import matplotlib.pyplot as plt

#data set
#input
#input data, features
# h(x) -> input data : x1 -> xn
x_train = [ np.random.rand() * 10 for _ in range(50)]
y_train = [ val + np.random.rand()* 5 for val in x_train]

# BGB (Batch Gradient Descent)
# 배치 경사 하강법을 이용하여 Linear regression적용
w = 0.0
leaning_rate = 0.01
epoch = 50
w_list = []
for num_of_epoch in range(epoch):
    gradient_sum = 0.0
    
    # GD 수행 후 최저의 W 값 도출
    for x, y in zip(x_train, y_train):
        # predict_value
        # 기울기 값
        gradient_sum += x * (w * x - y)
        
    # W값 업데이트
    print(gradient_sum)
    w = w - leaning_rate * (gradient_sum / len(x_train))
    
    w_list.append(w)

x_test = [val for val in range(10)]
y_test = [w * val for val in x_test]

# print(x_train)
# print("-" *100)
# print(y_train)
print(w_list)

plt.scatter(x_train, y_train, color = "blue")
plt.plot(x_test, y_test)
plt.show()
#output
#label
# f(x1) -> f(x2)