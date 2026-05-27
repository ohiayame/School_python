# 두 set 각각에 대해 `in` 으로 검사한 결과를 조합해 분기하세요.
club_a = {"윤서", "지우", "민준", "도윤"}
club_b = {"지우", "민준", "예준", "하준"}
name = input()

# 검사 결과를 변수로 저장해 중복 호출 없이 재사용
in_a = name in club_a
in_b = name in club_b

# if-elif-else 체인으로 네 가지 경우를 명확하게 분기
if in_a and in_b:
    result = "양쪽 모두"
elif in_a:
    result = "A 동아리만"
elif in_b:
    result = "B 동아리만"
else:
    result = "미가입"

# 결과 값 출력
print(result)