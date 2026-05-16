# for + 누적 변수를 사용하세요.
n = int(input())
# 누적 변수 정의
total = 0

# for문으로 누적 계산
for num in range(1, n + 1):
    total += num 

# 결과 값 출력
print(f"1부터 {n}까지의 합: {total}")