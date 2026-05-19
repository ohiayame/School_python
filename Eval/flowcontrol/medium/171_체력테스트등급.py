# 횟수에 따라 등급을 구분하세요
count = int(input())

# 60회 이상: A
if count >= 60:
    grade = "A"
# 45회 이상: B
elif count >= 45:
    grade = "B"
# 30회 이상: C
elif count >= 30:
    grade = "C"
# 15회 이상: D
elif count >= 15:
    grade = "D"
# 15회 미만: F
else:
    grade = "F"

# 결과 값 출력
print(f"횟수: {count}회 → 등급: {grade}")