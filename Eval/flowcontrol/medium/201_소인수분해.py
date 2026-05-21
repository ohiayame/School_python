# 정수를 소인수분해하여 결과를 출력하세요.
n = int(input())

div = 2
prime_factors = []

# 소인수분해 계산
# n이 1이 될 때까지 반복
while n > 1:
    # 나눌 수 있는 값이 있으면
    if n % div == 0:
        # div를 prime_factors에 저장하고 n값 // div로 n를 갱신
        prime_factors.append(div)
        n //= div
    # 아니면 나누는 값을 +1
    else:
        div += 1

# 결과 값 출력
print(" x ".join(map(str, prime_factors)))