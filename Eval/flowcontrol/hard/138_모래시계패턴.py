2# 모래시계 패턴을 출력하세요.
n = int(input())
mid_row = n // 2 + 1  # 변수명을 herf -> mid_row 로 수정 (중간 행 번호)

def print_row(row):
    """행 번호를 받아 공백과 별을 출력하는 헬퍼 함수"""
    spaces = mid_row - row  # 왼쪽 공백 수
    stars = n - spaces * 2  # 별 개수
    print(" " * spaces + "*" * stars)

# 위의 역삼각형 출력
for row in range(mid_row, 0, -1):
    print_row(row)

# 아래쪽 삼각형 출력 (가운데 행 제외, 2행부터 시작)
for row in range(2, mid_row + 1):
    print_row(row)