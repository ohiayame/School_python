"""
[문제]
    숫자 N을 입력받아 
    1부터 N까지의 합을 (1부터 N까지의 합: 합계) 형식(f-string)으로 출력하시오.
    i = 1, while i <= n: total += i; i += 1
"""

n = int(input())
total = 0
i = 1

# i가 n이하일 때 반복
while i <= n:
    # total에 i 추가
    total += i
    # i에 1추가
    i += 1

# 1부터 N까지의 합: 합계 형식으로 출력
print(f"1부터 {n}까지의 합: {total}")