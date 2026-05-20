# 각 행을 차례로 방문하면서 `grid[i][c]` 를 모아 출력하세요.
grid = [
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
col = int(input())

# grid를 반복하여 입력받은 col번째 원소 수집
column_values = [row[col] for row in grid]  # range(len) 대신 직접 행 순회

# join으로 출력하면 trailing space 없이 깔끔하게 출력됨
print(" ".join(map(str, column_values)))