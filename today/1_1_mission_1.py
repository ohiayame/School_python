# 나이에 따라 다양한 이용권을 제공
# 사용자의 나이를 입력받는다
age = int(input("사용자의 나이를 입력해주세요: "))

# 입력받은 나이에 따라 적합한 도서관 이용권을 판별하여, 결과를 출력
# 어린이 이용권: 12세 이하
if age <= 12:
    print("어린이 이용권을 사용할 수 있습니다.")
    
# 청소년 이용권: 13세에서 18세 사이
elif age <= 18 :
    print("청소년 이용권을 사용할 숫 있습니다.")
    
# 성인 이용권: 19세 이상
elif 19 <= age :
    print("성인 이용권을 사용할 숫 있습니다.")