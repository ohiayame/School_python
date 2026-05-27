# 소수인지 검증하여 bool형으로 반환
def prime_check(n):
    # 2면 소수 -> 3이상이면 소수 검증
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# N을 두 소수의 합으로 표현하는 모든 경우를 출력하세요.
N = int(input()) # 입력은 항상 4 이상의 짝수

for num in range(2, N // 2 + 1):
    # num이 소수이면 N - num 값이 소수인지 검증 둘다 소수면 출력
    if prime_check(num) and prime_check(N - num):
            print(f"{N} = {num} + {N - num}")