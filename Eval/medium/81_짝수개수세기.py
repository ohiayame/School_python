# for + if + 카운팅 변수를 사용하세요.
n = int(input())
total = 0

# 1부터 N까지 반복
for num in range(1, n + 1):
    # 짝수이면 total에 추가
    if num % 2 == 0:
        total += 1

# 결과 값 출력
print(f"1부터 {n}까지 짝수의 개수: {total}")