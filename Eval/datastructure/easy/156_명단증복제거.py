# set 으로 중복 제거 + 정렬 + 출력.
data_sets = [
    ["윤서", "지우", "민준", "윤서", "도윤", "지우", "예준"],
    ["A", "B", "C"],
    ["혼자", "혼자", "혼자"],
]
t = int(input())
names = data_sets[t]

# set 으로 변환하면 자동 중복 제거 + sorted로 정렬
unique_names = sorted(set(names))

# 결과 값 출력
print(f"총 {len(unique_names)}명")
print(*unique_names)