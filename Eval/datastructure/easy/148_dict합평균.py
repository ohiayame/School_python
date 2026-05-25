# 합 계산 후 평균은 합 / 길이.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 합계와 평균 계산 후 출력
total = sum(scores.values())
avg = total / len(scores)

print(f"합계: {total}")
print(f"평균: {avg:.1f}")