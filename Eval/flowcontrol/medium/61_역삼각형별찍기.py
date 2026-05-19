# range(n, 0, -1)은 n부터 1까지 감소합니다.
n = int(input())

# 줄 수 N만큼 반복 (n부터 1까지 감소)
for counter in range(n, 0, -1):
    # 별 출력
    print("*" * counter)