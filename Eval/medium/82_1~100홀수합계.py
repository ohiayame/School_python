# for + if + 누적 변수를 사용하세요.
total = 0
MAX_VALUE = 100

for num in range(1, MAX_VALUE + 1):
    # 홀수이면 total에 추가
    if num % 2 == 1:
        total += num

print(f"1부터 {MAX_VALUE}까지 홀수의 합: {total}")