# 숫자와 N을 입력받아 2~N의 배수인지 각각 출력하세요.
num = int(input())
n = int(input())

# 2 ~ n까지 반복
for val in range(2, n + 1):
    # num이 i의 배수(num % val == 0)면 "val의 배수입니다." 출력
    if num % val == 0:
        print(f"{val}의 배수입니다.")
    # 아니면 "{val}의 배수가 아닙니다." 출력"
    else:
        print(f"{val}의 배수가 아닙니다.")