# 위쪽 삼각형과 아래쪽 역삼각형을 각각 for문으로 출력하세요.
n = int(input())

def print_row(total, i):
    # 공백 (N-i)개 + 별 (2*i-1)개를 출력하는 공통 함수로 추출
    print(" " * (total - i) + "*" * (2 * i - 1))

# 위쪽 삼각형 1~n번
for row_up in range(1, n + 1):
    print_row(n, row_up)

# 아래쪽 역삼각형 n-1 ~ 0로 역순회
for row_down in range(n-1, 0, -1):
    print_row(n, row_down)