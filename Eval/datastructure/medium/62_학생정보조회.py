# `for name, score in students:` 형태로 각 tuple을 두 변수로 한 번에 받아 순회하세요.
students = [
    ("윤서", 85),
    ("지우", 92),
    ("민준", 65),
    ("서윤", 78),
    ("도윤", 95),
]
target = input()
is_not_std = True # 학생 없음 상태로 플래그 정의

# students 순회
for name, score in students:
    # 이름이 있으면 점수 출력하고 플래그 false로 변경후 순회 종료
    if name == target:
        print("점수:", score)
        is_not_std = False
        break

# 학생이 없었으면 학생 없음 출력
if is_not_std:
    print("학생 없음")