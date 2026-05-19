#  i번째 줄에 1부터 i까지의 숫자를 이어붙여 출력하는 숫자 피라미드를 출력
# print(j, end="")을 사용해 줄바꿈 없이 이어서 출력하세요.

n = int(input())

# n번 반복 (줄)
for row in range(1, n + 1):
    # i번째 줄에 print(j, end="")을 사용해 줄바꿈 없이 숫자를 출력
    for num in range(1, row + 1):
        print(num, end="")
    # 한 줄마다 개행이 필요
    print()