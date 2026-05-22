# 0번째부터 N번째 피보나치 수를 출력하세요.
n = int(input())
print(f"피보나치 수열 (0~{n}번째):")

# 피보나치 초기값: current=F(0), next_val=F(1)
current = 0
next_val = 1

# N+1개 항을 순서대로 출력하며 값을 갱신
for _ in range(n + 1):  # 루프 변수를 사용하지 않으므로 _ 사용
    print(current, end=" ")
    current, next_val = next_val, current + next_val