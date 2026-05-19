# 누적 곱 변수의 초깃값은 1로 두고, 
# count번 반복하며 입력받은 숫자를 곱하세요.
count = int(input())

# 누적 곱 변수 (1로 초기화)
total = 1

# count번 반복
for _ in range(count):
    # 곱할 숫자 입력받기
    num = int(input())
    # 누적 곱 변수와 곱하여 재정의
    total *= num

# 누적 곱 결과 출력
print(f"누적 곱: {total}")