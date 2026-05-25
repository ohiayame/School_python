# set 변환 + sorted 로 한 번에 처리.
data_sets = [
    [85, 92, 65, 85, 95, 92, 78, 65],
    [1, 2, 3, 1, 2],
    [100, 100, 100],
]
t = int(input())
scores = data_sets[t]

# 1. set()으로 중복 제거
# 2. sorted()로 오름차순 정렬
# 3. 각 정수를 str()로 변환 후 공백으로 join하여 출력
print(" ".join(map(str, sorted(set(scores)))))