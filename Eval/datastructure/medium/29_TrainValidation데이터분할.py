# 두 슬라이스 `data[:k]` 와 `data[k:]` 로 한 번에 분할합니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
p = int(input())

# 분할 위치 계산
k = len(data) * p // 100

# 결과 값 출력
print("train:", *data[:k])
print("val:", *data[k:])