# if/elif/else로 등급을 판정하세요.
score = int(input())

# 규칙
"""
90 이상: A
80 이상: B
70 이상: C
60 이상: D
60 미만: F
"""
# 등급의 초기 값을 F로 정의
rank = "F"

# 입력 점수에 따른 등급을 저장
if score >= 90:
    rank = "A"
elif score >= 80:
    rank = "B"
elif score >= 70:
    rank = "C"
elif score >= 60:
    rank = "D"

# 결과 출력
print(f"점수: {score}")
print(f"등급: {rank}")