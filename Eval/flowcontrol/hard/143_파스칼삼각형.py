# 각 줄에서 이항계수를 누적 곱으로 계산하세요.
n = int(input())

for row in range(n):
    # 먼저 공백 출력
    print(" " * (n - 1 - row), end="")

    # 출력 값을 1로 초기화
    coef = 1

    # 각 줄의 숫자를 리스트에 수집한 뒤 join으로 출력 → trailing space 방지
    values = []
    for k in range(row + 1):
        values.append(str(coef))
        # 다음 값 = 이전 값 * (줄번호 - k) // (k + 1) 로 coef 값 갱신
        coef = coef * (row - k) // (k + 1)

    print(" ".join(values))