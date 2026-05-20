# 컴프리헨션 표현식 안에서 `min(...)` 을 호출해 한 번에 처리.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 70],
    [100],
]
t = int(input())
scores = data_sets[t]

# 각 점수에 10점을 더하되 100점을 넘기면 100으로 자른(clip) 결과
clipped_scores = [min(score + 10, 100) for score in scores]
print(" ".join(str(x) for x in clipped_scores))