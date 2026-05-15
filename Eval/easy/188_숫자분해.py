# 3자리 정수를 입력받아 백의자리, 십의자리, 일의자리로 분해하고, 
# 세 자리의 합과 곱을 출력하세요.
num = int(input())

# 백의자리 수 계산
hundred = num // 100
# 십의자리 수 계산
ten = (num % 100) // 10
# 일의자리 수 계산
one = num % 10

# 계산 결과를 출력
print(f"백의자리: {hundred}")
print(f"십의자리: {ten}")
print(f"일의자리: {one}")
print(f"합: {hundred + ten + one}")
print(f"곱: {hundred * ten * one}")