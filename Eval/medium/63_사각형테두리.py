n = int(input())

# n줄 반복
for row in range(n):
    # 첫번째 줄과 마지막 줄은 n개의 별표 출력
    if row == 0 or row == n - 1:
        print("*" * n)
    # 아니면(중간 줄) (별표 + (n - 2)의 공백 + 별표) 출력
    else:
        print(f"*{' ' * (n - 2)}*")