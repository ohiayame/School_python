# 최댓값 위치를 찾아 이름 리스트에서 같은 인덱스 학생 출력.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["X", "Y"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 점수가 가장 높은 학생의 이름을 한 줄로 출력
# 1) 최고점 인덱스 구하기 → 2) 해당 이름 출력
# 동점 시 앞 학생 우선 — index()가 첫 등장값 반환
best_index = scores.index(max(scores))  # 한 번에 최고점 위치 확정
print(names[best_index])