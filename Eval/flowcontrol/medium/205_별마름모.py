# 홀수 N을 입력받아 마름모를 출력하세요.
n = int(input())

mid_row = n // 2 + 1  # 변수명을 herf -> mid_row 로 수정 (중간 행 번호)

# 2개로 나눠서 출력
for row in range(1, mid_row + 1):
    spaces = mid_row - row
    stars = n - spaces * 2
    print(" " * spaces + "*" * stars)  # 후행 공백 제거

for row in range(mid_row - 1, 0, -1):
    spaces = mid_row - row
    stars = n - spaces * 2
    print(" " * spaces + "*" * stars)  # 후행 공백 제거