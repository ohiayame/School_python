# 1부터 N 사이의 카프리카 수를 찾아 출력하세요.
n = int(input())

print("카프리카 수:")

for num in range(1, n + 1):
    # 1은 특수 케이스
    if num == 1:
        print(1)
        continue

    square = num * num
    digit = len(str(num))

    # 오른쪽 부분은 num의 자리수만큼 자름
    power = 10 ** digit

    L = square // power
    R = square % power

    # 오른쪽 부분이 0이면 제외
    if R == 0:
        continue

    if L + R == num:
        # R은 자리수에 맞춰 0으로 채움
        R_str = str(R).zfill(digit)
        print(f"{num}: {num}^2 = {square}, {L} + {R_str} = {num}")