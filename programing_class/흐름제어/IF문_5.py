# 키보드로부터 영문 문자열을 입력 받아, 아래 테이블 규칙을 따라
# 한글로 변환하는 프로그램을 작성하라.
# 단, 아래 테이블 이외의 영문 이름이 입력 될 경우 “그 외” 문자열 출력
input_name = input()
if input_name == "SAMSUNG":
    print("삼성")
elif input_name == "NAVER":
    print("네이버")
elif input_name == "LG":
    print("엘쥐")
elif input_name == "HYUNDAI":
    print("현대")
elif input_name == "KAKAO":
    print("카카오")
elif input_name == "SK":
    print("에스케이")
else:
    print("그 외")