# for + range(1, n+1)로 누적합을 구한 뒤, 
# print("1부터", n, "까지의 합:", total)로 출력하세요.
n = int(input())

# 누적 계산
total = 0

for i in range(1, n + 1):
    total += i

# 결과 값 출력
print("1부터", n, "까지의 합:", total)