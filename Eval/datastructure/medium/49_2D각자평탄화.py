# 한 줄에 두 개의 for 를 두는 이중 컴프리헨션을 사용하세요.
grids = [
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
    [[1, 2, 3], [4, 5, 6]],
    [[1], [2], [3]],
]
t = int(input())
grid = grids[t]

# 이중 for 컴프리헨션으로 2D 리스트 ->  1차원 리스트
data = [num for row in grid for num in row]
# 공백 구분으로 한 줄에 출력
print(*data)