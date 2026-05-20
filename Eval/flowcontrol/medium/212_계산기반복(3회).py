def calculation(operator, num1, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    else:
        result = num1 // num2
    return  result

# 3번 반복하며 계산 결과를 누적하세요.
total = 0
count = 3

# 3번 반복
for _ in range(count):
    # 입력 받기 (항상 "숫자1 연산자 숫자2" 형태)
    num1, operator, num2 = input().split()
    # 계산후 출력
    result = calculation(operator, int(num1), int(num2))
    print(result)
    # 합계 계산
    total += result

# 합계 출력
print(f"합계: {total}")