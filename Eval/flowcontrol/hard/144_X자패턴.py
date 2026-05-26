# 행과 열을 순회하면서 대각선 조건을 확인하세요.
n = int(input())

for row in range(n):
    row_str = ""
    for col in range(n):
        # 행 i, 열 j에서 i == j 또는 i + j == n - 1이면 대각선
        is_diagonal = (row == col) or (row + col == n - 1)  # 조건을 변수로 분리해 명확성 향상
        row_str += "*" if is_diagonal else " "  # 아니면 공백
    # 행 종료시 줄바꿈 (print 호출 횟수 최소화)
    print(row_str)