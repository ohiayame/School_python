# 1부터 N 사이의 친화수 쌍을 출력하세요.
N = int(input())

def proper_divisor_sum(num):
    """num의 진약수(자기 자신 제외 약수)의 합을 반환합니다."""
    if num < 2:
        return 0
    divisor_sum = 1  # 1은 항상 진약수
    # √num까지만 순회해 약수 쌍을 동시에 처리 → O(√N)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:  # 중복 방지 (완전제곱수 처리)
                divisor_sum += num // i
    return divisor_sum


for a in range(1, N + 1):
    b = proper_divisor_sum(a)

    # a != b : 완전수 제외
    # a < b : 같은 쌍을 두 번 출력하지 않기 위해
    # b <= N : 1부터 N 사이의 쌍만 출력하기 위해
    if a < b <= N and proper_divisor_sum(b) == a:
        print(f"({a}, {b})")