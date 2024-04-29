# 사용자로부터 세 개의 정수 숫자를 입력받는다
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))

# 입력받은 숫자들 중 가장 큰 숫자를 판별
bignum = max(num1,num2,num3)  

# 가장 큰 숫자를 출력
print("가장 큰 숫자는", str(bignum)+ "입니다.")