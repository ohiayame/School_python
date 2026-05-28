# 공백 + 숫자 순순회 + 숫자 역순회 문자열 계산 후 반환 함수
def make_diamond_row(row):
    spaces = mid_row - row
    digit_count = n - spaces * 2  # 변수명을 nums -> digit_count 로 변경 (함수명과 혼동 방지)
    half = digit_count // 2  # 중간 계산값을 변수로 분리해 가독성 향상
    ascending = ''.join(str(num) for num in range(1, half + 2))
    descending = ''.join(str(num) for num in range(half, 0, -1))
    return f"{' ' * spaces}{ascending}{descending}"

# 숫자 다이아몬드를 출력하세요.
n = int(input())
mid_row = n // 2 + 1  # 중간 행 번호

# 위의 삼각형 출력
for row in range(1, mid_row):
    print(make_diamond_row(row))

# 밑의 역삼각형 출력
for row in range(mid_row, 0, -1):
    print(make_diamond_row(row))