# (i + j) % 2로 판정하세요.
# 알고리즘: 이중 반복으로 각 셀 판정 → 행 단위로 묶어 출력
n = int(input())

for row in range(n):
    # 각 열의 문자를 리스트로 모아 공백으로 연결해 출력 (end 분기 불필요)
    row_cells = ["#" if (row + col) % 2 == 0 else "." for col in range(n)]
    print(" ".join(row_cells))