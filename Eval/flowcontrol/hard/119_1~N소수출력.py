# 2부터 N까지 각 수가 소수인지 판별하여 출력하세요.
n = int(input())

prime_count = 0

# 2 ~ n까지의 값이 소수인지 검증
for num in range(2, n + 1):
    is_prime = True  # 소수 플래그

    # 각 숫자 소수 검증
    for i in range(2, int(num ** 0.5) + 1):
        # 나눌 수 있으면 종료
        if num % i == 0:
            is_prime = False
            break

    # 소수면 total + 1하고 출력 / 끝에 공백 포함-> end=" "
    if is_prime:
        prime_count += 1
        print(num, end=" ")
        
# 소수 개수: K 형식으로 소수 개수를 출력
print(f"\n소수 개수: {prime_count}")