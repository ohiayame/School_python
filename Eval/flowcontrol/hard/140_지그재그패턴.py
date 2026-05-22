# 지그재그 패턴을 출력하세요.
n = int(input())
m = int(input())

# 각 줄(row)에 해당하는 숫자를 바로 생성해 출력 (별도 배열 불필요)
for row_idx in range(n):
    # 현재 줄에 출력할 숫자 범위 계산
    row_nums = range(row_idx * m + 1, (row_idx + 1) * m + 1)

    # 짝수 줄(0-based 홀수 인덱스)은 2*m 칸 들여쓰기
    if row_idx % 2 == 1:
        print(" " * (2 * m) + " ".join(map(str, row_nums)))
    else:
        print(*row_nums)