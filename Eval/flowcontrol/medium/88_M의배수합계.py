# for + if(i % m == 0) + 누적 변수를 사용하세요.
n = int(input())
m = int(input())

#  1부터 N까지 중 M의 배수의 합 저장 변수
total = 0

# n번 반복
for num in range(1, n + 1):
    # M의 배수의 합 계산
    if num % m == 0:
        total += num

# 출력 형식: 1부터 N까지 M의 배수의 합: 값
print(f"1부터 {n}까지 {m}의 배수의 합: {total}")