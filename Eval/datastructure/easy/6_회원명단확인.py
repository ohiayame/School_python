# 리스트 멤버십 검사에는 `in` 연산자를 사용합니다.
members = ["윤서", "지우", "민준", "서윤", "도윤"]
name = input()

# 리스트 멤버십 검사에는 `in` 연산자를 사용
# 조건에 맞게 결과를 출력
if name in members:
    print("있음")
else:
    print("없음")