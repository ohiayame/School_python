import matplotlib.pyplot as plt

# 데이터 준비
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 선 그래프 그리기
# plt.plot(x, y)

# 산점도 그래프
# plt.scatter(x, y)

# 막대 그래프
# plt.bar(x, y)

# 히스토그램
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4)

# 제목과 축 레이블 추가
plt.title("Sample Plot")
plt.xlabel("x")
plt.ylabel("y")

# 그래프 보여주기
plt.show()
