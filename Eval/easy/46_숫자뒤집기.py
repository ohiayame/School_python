# 양의 정수를 입력받아 
# 숫자를 뒤집어서 (뒤집은 숫자: 값) 형식(f-string)으로 출력하시오.
# 힌트: digit = num % 10, reverse = reverse * 10 + digit, num //= 10
# while num > 0으로 반복하며 마지막 자리를 꺼내 reverse에 쌓으세요.

num = int(input())
reverse = 0

# num이 없어질때 까지 반복
while num > 0:
    # 마지막 숫자 추출
    digit = num % 10
    # reverse를 10곱하고 1의 位에 digit 저장
    reverse = reverse * 10 + digit
    # num의 1의 位 지우기
    num //= 10

# 결과 값을 (뒤집은 숫자: 값) 형식으로 출력
print(f"뒤집은 숫자: {reverse}")