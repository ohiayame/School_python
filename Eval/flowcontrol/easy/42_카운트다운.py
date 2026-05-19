"""
[문제]
    시작 숫자 N을 입력받아 
    N부터 1까지 줄바꿈하며 출력
    출력한 뒤 마지막에 발사!를 출력하시오.
    while n >= 1: print(n); n -= 1 후 "발사!" 출력.
"""
n = int(input())

# N부터 1까지 while n >= 1: 로 반복
while n >= 1:
    # n 출력
    print(n)
    #  n -= 1
    n -= 1

# "발사!" 출력
print("발사!")