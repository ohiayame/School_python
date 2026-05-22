# 출력 시 set 을 정렬해 일관된 순서로 표시.
a_sets = [
    {"윤서", "지우", "민준"},
    {"a", "b", "c"},
    {"1", "2", "3"},
]
b_sets = [
    {"지우", "도윤", "예준"},
    {"x", "y", "z"},
    set(),
]
t = int(input())
a = a_sets[t]
b = b_sets[t]
# 합집합 계산: 두 set의 모든 원소를 하나로 합침
union_set = a | b 

print(" ".join(sorted(union_set)))