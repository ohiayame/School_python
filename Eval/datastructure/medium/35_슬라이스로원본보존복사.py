# 사본을 만든 후 사본에만 정렬을 적용해야 원본이 보존됩니다.
data_sets = [
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [5, 3, 1],
    [7],
]
t = int(input())
original = data_sets[t]

# 원본 현재 상태
print("원본:", *original)

# 사본을 만들어 정렬
copy = original[:]
copy.sort()
# 정렬된 사본 출력
print("정렬:", *copy)
# 원본 최종 상태 출력
print("원본:", *original)