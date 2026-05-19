# 공백을 먼저 (n-i)개 출력한 뒤 별을 i개 출력하세요.
n = int(input())

# 1~n번 반복
for star_count in range(1, n + 1):
    # " "(n - i)개 뒤에 "*" i개 출력
    print(" " * (n - star_count) + "*" * star_count)