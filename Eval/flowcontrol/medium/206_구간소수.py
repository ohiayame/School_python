# 구간 내 소수를 찾아 출력하세요.
start = int(input())
end = int(input())
primes = []

for num in range(start, end + 1):  # end 포함을 위해 end+1 로 수정
    # 소수 플래그
    is_prime = True
    # 1 초과 시만 계산
    if num > 1:
        # 제곱근까지만 검사해도 소수 판별 가능 (O(√n) 최적화)
        for i in range(2, int(num**0.5) + 1):
            # 나눌 수 있으면(소수가 아님) -> is_prime를 False로 수정하고 종료
            if num % i == 0:
                is_prime = False
                break
        # 소수이면 primes에 추가
        if is_prime:
            primes.append(num)

# 결과 값 출력
print(*primes)