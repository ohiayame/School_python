# 각 그룹 list 를 빌딩 후 빈 경우 라벨만 출력.
s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95, "예준": 60},
    {"A": 85, "B": 95, "C": 75},
    {"Y": 60},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# s1 키 순회로 only1, both / s2 키 순회로 only2 를 분류
only1 = []
only2 = []
both = []
both_set = set()  # O(1) 조회를 위해 set 별도 관리

for name in s1:
    if name in s2:
        both.append(name)
        both_set.add(name)
    else:
        only1.append(name)

for name in s2:
    if name not in both_set:  # 리스트 대신 set으로 O(1) 조회
        only2.append(name)

# 결과 값을 출력 — 빈 경우 라벨 뒤 공백 없이 출력
def fmt(label, lst):
    return label + (' ' + ' '.join(lst) if lst else '')  # 빈 리스트면 공백 생략

print(fmt('1학기만:', only1))
print(fmt('2학기만:', only2))
print(fmt('양학기:', both))