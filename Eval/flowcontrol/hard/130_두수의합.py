# 합이 target인 두 수의 쌍을 출력하세요.
N = int(input())
target = int(input())

# (a < b) 범위로 반복
for num1 in range(1, N // 2 + 1):
    num2 = target - num1
    if num1 < num2 <= N:
        print(f"({num1}, {num2})")