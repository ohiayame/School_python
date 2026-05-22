# `set(list)` 로 변환하면 중복이 자동 제거됩니다.
datasets = [
    ["apple", "banana", "apple", "cherry"],
    [1, 2, 1, 2, 1, 2, 3],
    ["A", "B", "C", "D", "E"]
]
t = int(input())

# 중복을 제거한 뒤 고유 원소 개수를 출력
print(len(set(datasets[t])))