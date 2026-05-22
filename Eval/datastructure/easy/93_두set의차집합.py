# 방향 중요 — 학생은 a - b 임을 확인.
a_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"a", "b", "c", "d"},
    {"x", "y"},
]
b_sets = [
    {"지우", "도윤", "예준"},
    {"c", "d", "e"},
    {"x", "y", "z"},
]

scenario_idx = int(input())
set_a = a_sets[scenario_idx]
set_b = b_sets[scenario_idx]

# 차집합을 정렬해 공백 구분 한 줄에 출력
difference_set = set_a - set_b
print(" ".join(sorted(difference_set)))