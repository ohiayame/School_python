# 교집합이 비면 자연스럽게 빈 줄.
s1_sets = [
    {"윤서", "지우", "민준", "도윤"},
    {"A", "B", "C"},
    {"X", "Y"},
]
s2_sets = [
    {"지우", "도윤", "예준", "하준"},
    {"A", "B"},
    {"P", "Q"},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 교집합 출력: s1 & s2 + sorted 후 " ".join 결과가 빈 문자열
print(" ".join(sorted(s1 & s2)))