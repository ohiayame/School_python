# 묵시적 형변환
value_int = int(input("첫 번째 숫자(정수)를 입력하세요: "))
value_float = float(input("첫 번째 숫자(부동 소수점 수)를 입력하세요: "))

# 두 수의 합이 100을 초과하는지 검사
if (value_int + value_float) > 100 :
    msg = "합이 100을 초과합니다:"
else:
    msg = "합이 100 이하입니다:"
    
print(msg,(value_int + value_float))

