# 먼저 등급을 판별한 뒤 수료 여부를 판단하세요.
score = int(input())
attendance = int(input())

grade = ""    # 등급 저장 변수
result = ""   # 수료 여부 문자 저장 변수


# 90점 이상: A
if score >= 90:
    grade = "A"
# 80점 이상: B
elif score >= 80:
    grade = "B"
# 70점 이상: C
elif score >= 70:
    grade = "C"
# 60점 이상: D
elif score >= 60:
    grade = "D"
# 60점 미만: F
else:
    grade = "F"

# 등급이 F면: 미수료 - 성적 미달 (60점 이상 필요) 
if grade == "F":
    result = "미수료 - 성적 미달 (60점 이상 필요)"
# 등급이 F가 아니고 출석률 < 80이면: 미수료 - 출석률 부족 (80% 이상 필요) 
elif attendance < 80:
    result = "미수료 - 출석률 부족 (80% 이상 필요)"
# 그 외: 수료를 축하합니다! 
else:
    result = "수료를 축하합니다!"

# 결과 값 출력
print(f"등급: {grade}\n{result}")