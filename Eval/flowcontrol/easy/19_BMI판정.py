# cm를 m로 변환한 후 BMI = weight / (height_m ** 2). round(bmi, 2) 사용.
height = float(input())
weight = float(input())

# BMI 계산: 몸무게 / (키/100)^2 (소수 둘째 자리까지)
bmi = round(weight / ((height / 100) ** 2), 2)

# 판정을 비만으로 초기화
verdict = "비만"

# 조건에 맞춰서 판정 정의
# 1. BMI가 18.5 미만이면 "저체중"
if bmi < 18.5:
    verdict = "저체중"
# 2. BMI가 23 미만이면 "정상"
elif bmi < 23:
    verdict = "정상"
# 3. BMI가 25 미만이면 "과체중"
elif bmi < 25:
    verdict = "과체중"

# 결과 출력
print(f"키: {height}cm, 몸무게: {weight}kg")
print(f"BMI: {bmi}")
print(f"판정: {verdict}")