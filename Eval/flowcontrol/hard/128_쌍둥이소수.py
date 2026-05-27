# 1부터 N 사이의 쌍둥이 소수 쌍을 출력하세요.
num = int(input())

prime = 0 # 소수 임시저장 변수

for n in range(3, num + 1):
    # 소수 검증
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    # 소수이면
    if is_prime:
        # 이전의 소수 + 2 와 현재 값이 같으면 출력
        if prime + 2 == n:
            print(f"({prime}, {n})")
        # prime 값 갱신
        prime = n