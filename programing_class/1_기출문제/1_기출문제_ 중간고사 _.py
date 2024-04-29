# 출력 (첫 번째 값을 입력 하세요)
print("첫 번째 값을 입력 하세요")
# 1 실수를 입력받기
value1 = input()
# 출력 (두 번째 값을 입력 하세요
print("두 번째 값을 입력 하세요")
# 2 실수를 입력받기
value2 = input()

# 출력 (연산자를 선택 하세요 (+, -, *, / 중 하나 입력)
print("연산자를 선택 하세요 (+, -, *, / 중 하나 입력)")
# 연산자를 입력 받기( +, -, *, / 중 하나 입력)
operator = input()
# if  + 를 입력 받았을 때
if operator ==  "+":
    result_value = float(value1) + float(value2)
# elif - 를 입력 받았을 때
elif operator == "-":
    result_value = float(value1) - float(value2)
# elif * 를 입력 받았을 때
elif operator == "*":
    result_value = float(value1) * float(value2)
# elif / 를 입력 받았을 때
# -> 예외 처리 필요 없으니까 else사용
else:
    result_value = float(value1) / float(value2)
    
# 출력 (결과 값 자료형(integer, float, string 중 하나 입력)
print("결과 값 자료형(integer, float, string 중 하나 입력)")
# 결과 값 자료형을 입력 받기(integer, float, string 중 하나 입력)
input_type = input()
# if  integer 를 입력 받았을 때
if input_type == "integer":
    result_value = int(result_value)
# elif float 를 입력 받았을 때
elif input_type == "float":
    result_value = float(result_value)
# elif string 를 입력 받았을 때
# -> 예외 처리 필요 없으니까 else사용
else:
    result_value = str(result_value)
    
# 출력 ( 결과 값은 아래와 같습니다.
print("결과 값은 아래와 같습니다.")
# 1 (연산자) 2 = 결과값 출력 
print(value1, operator, value2, "=", result_value)