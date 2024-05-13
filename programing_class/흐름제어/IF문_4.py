# 0 이면 “0” 를 문자열로 출력
# 양수이면 “양수"를 문자열로 출력
# 음수 이면 "음수" 문자열을 화면에 출력
value = int(input("정수를 입력 하세요"))
if value > 0:
    print("양수 입니다.")
elif value == 0:
    print("0 입니다.")
else:
    print("음수 입니다.")