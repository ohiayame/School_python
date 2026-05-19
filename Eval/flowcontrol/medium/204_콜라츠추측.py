# 콜라츠 추측 과정과 횟수를 출력하세요.
n = int(input())
print(n)

# 1이 될 때까지 짝수→÷2, 홀수→×3+1 반복
step_count = 0
while n > 1:
    # 짝수이면 2로 나눈다
    if n % 2 == 0:
        n //= 2
    # 홀수이면 3을 곱하고 1을 더한다
    else:
        n = n * 3 + 1
    print(n)
    step_count += 1  # 변환 후 단계 카운트

# 결과 값 출력
print("횟수:", step_count)