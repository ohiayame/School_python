def make_diamond_row(row, n, half):
    """다이아몬드의 한 줄을 출력합니다."""
    if row == 1:
        # 꼭짓점: 별 하나만, trailing space 없이
        print(" " * (half - row) + "*")
    else:
        spaces = half - row
        # 양쪽 별 사이 공백 = n에서 양쪽 공백과 별 2개를 뺀 값
        inner = n - (spaces * 2 + 2)
        print(" " * spaces + "*" + " " * inner + "*")

# 빈 다이아몬드를 출력하세요.
n = int(input())

half = n // 2 + 1  # 중앙 줄까지의 행 수 (herf → half 오타 수정)

# 상단 절반 (꼭짓점 ~ 중앙)
for i in range(1, half):
    make_diamond_row(i, n, half)

# 하단 절반 (중앙 ~ 꼭짓점)
for i in range(half, 0, -1):
    make_diamond_row(i, n, half)