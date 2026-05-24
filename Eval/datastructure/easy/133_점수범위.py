# max 와 min 의 차이를 직접 출력.
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# 최고점과 최저점의 차이를 한 줄로 출력
print(max(scores) - min(scores))