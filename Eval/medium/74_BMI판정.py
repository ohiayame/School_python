# 나이로 기준을 먼저 나누세요.
height = float(input())
weight = float(input())
age = int(input())

# BMI 계산
bmi = weight / ((height / 100) ** 2)
result = ""

# 성인(age >= 20):
if age >= 20:
    # < 18.5: 판정: 저체중
    if bmi < 18.5:
        result = "저체중"
    # < 23: 판정: 정상
    elif bmi < 23:
        result = "정상"
    # < 25: 판정: 과체중
    elif bmi < 25:
        result = "과체중"
    # 그 외: 판정: 비만
    else:
        result = "비만"

# 청소년(age < 20):
else:
    # < 17: 판정: 저체중 (청소년 기준)
    if bmi < 17:
        result = "저체중 (청소년 기준)"
    # < 23: 판정: 정상 (청소년 기준)
    elif bmi < 23:
        result = "정상 (청소년 기준)"
    # 그 외: 판정: 과체중 주의 (청소년 기준)
    else:
        result = "과체중 주의 (청소년 기준)"

# 결과 출력
print(f"BMI: {round(bmi, 2)}")
print(f"판정: {result}")