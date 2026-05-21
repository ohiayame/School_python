# 2 이상의 정수를 입력받아 소수 여부를 판별하세요.
num = int(input())
is_prime = True    # 소수 여부 플래그

# 소수인지 검증
# for i in range(2, num):
for i in range(2, int(num**0.5) + 1):
    # 나눌 수 있으면 is_prime = False 후 종료
    if num % i == 0:
        is_prime = False
        break

# 상태에 따라 결과 값 출력
if is_prime:
    print(f"{num}은(는) 소수입니다.")
else:
    print(f"{num}은(는) 소수가 아닙니다.")
