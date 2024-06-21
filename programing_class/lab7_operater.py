# 덧셈, 뺄셈, 곱셈, 나눗셈 계산기
# 사용자로부터 2정수 입력받는다
inputvalue_1 = int(input("첫 번째 숫자를 입력하세요: "))
inputvalue_2 = int(input("두 번째 숫자를 입력하세요: "))

# +, -, *, / 결과를 출력
print('합: ' , float(inputvalue_1 + inputvalue_2))
print('차: ' , float(inputvalue_1 - inputvalue_2))
print('곱: ' , float(inputvalue_1 * inputvalue_2))
print('나눗셈: ' , float(inputvalue_1 / inputvalue_2))