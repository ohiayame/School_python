# `not in` 으로 명단에 없는 경우를 먼저 분기하세요.
attendance = ["윤서", "민준", "도윤", "예준"]
name = input()

# `not in` 으로 명단에 없는 경우를 먼저 분기
# 조건에 맞게 결과 출력
if name not in attendance:
    print("결석")
else:
    print("출석")