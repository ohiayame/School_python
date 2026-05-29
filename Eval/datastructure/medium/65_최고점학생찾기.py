# 추적 변수 두 개를 두고 for 순회로 비교 + 갱신.
data_sets = [
    [("윤서", 85), ("지우", 92), ("민준", 65), ("서윤", 78), ("도윤", 95)],
    [("A", 70), ("B", 90), ("C", 80)],
    [("solo", 70)],
]
t = int(input())
students = data_sets[t]

# 0번째로 초기화
top_name, top_score = students[0]

# 1번째 이후 비교하면서 top_name, top_score를 갱신
for name, score in students[1:]:
    if top_score < score:
        top_name, top_score = name, score

# 결과 값 출력
print(f"{top_name}: {top_score}")