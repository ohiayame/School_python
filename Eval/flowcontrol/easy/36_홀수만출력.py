# 1부터 N까지 반복하며 i % 2 == 1인 경우에만 print(i)로 출력하세요.
n = int(input())

# 1부터 N까지 반복
for i in range(1, n + 1):
    # 홀수인지 확인
    if i % 2 == 1:
        # 한 줄에 하나씩 출력
        print(i)