# chr(65)는 'A', chr(65+1)은 'B'입니다.
n = int(input())

# 1~n번 반복
for row in range(1, n + 1):
    # row만큼의 알파벳 출력 end=""로 연결
    for num in range(row):
        # chr(65 + num) 번째 알파벳 출력
        print(chr(65 + num), end="")
    # 줄바꿈 출력
    print()