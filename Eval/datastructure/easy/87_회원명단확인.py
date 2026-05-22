# `in` 연산자로 set 멤버십을 검사하세요.
members = {"윤서", "지우", "민준", "서윤", "도윤"}
name = input()

# name이 members에 포함되면 '있음', 아니면 '없음' 출력
print("있음" if name in members else "없음")