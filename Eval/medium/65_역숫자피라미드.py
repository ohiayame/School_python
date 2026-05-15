# range(i, 0, -1)로 i부터 1까지 역순 출력하세요.
n = int(input())

# n번 반복
for row in range(n):
    # n - row부터 역순으로 숫자 출력 
    for num in range(n - row, 0, -1):
        print(num, end="")
    # 줄바꿈 출력
    print()