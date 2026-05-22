# # 유클리드 호제법으로 GCD를 구하세요.
# a = int(input())
# b = int(input())

# # 첫 줄: GCD(a, b) 계산 과정: 출력
# print(f"GCD({a}, {b}) 계산 과정:")

# # 루프 조건을 명시해 종료 시점을 한눈에 파악 가능하게 함
# while b != 0:
#     remainder = a % b  # 변수명을 remainder로 변경해 의미를 명확히
#     print(f"  {a} ÷ {b} = {a // b} ... 나머지 {remainder}")
#     # a, b를 재정의
#     a = b
#     b = remainder

# print(f"최대공약수: {a}")


# 두 수의 GCD와 LCM을 출력하세요.
def gcd_function(num1, num2):  # 파라미터명을 num1, num2로 명확히
    """유클리드 호제법으로 두 정수의 최대공약수를 반환합니다."""
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1

# 1. 입력 받기
num_a = int(input())  # 의미 있는 변수명으로 개선
num_b = int(input())

# 2. GCD / LCM 계산
gcd = gcd_function(num_a, num_b)
lcm = num_a * num_b // gcd

# 3. 출력
print(f"최대공약수(GCD): {gcd}")
print(f"최소공배수(LCM): {lcm}")