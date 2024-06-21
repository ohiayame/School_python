# age
age = int(input("나이를 입력하세요: "))
# event_code
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
# reservation_date
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

# 날짜 통과 
if  1 <= reservation_date <= 30 :
    # 나이제한 통과
    if (event_code == "E1" and age < 18) or (event_code == "E3" and age < 16) :
        print("나이 제한으로 인해 예약할 수 없습니다.")
    # 날짜제한 통과    
    elif (event_code == "E3" and (not 0 == reservation_date % 7) ) or(event_code == "E2" and (not 0 == reservation_date % 2)):
        print("선택하신 날짜에는 예약할 수 없습니다.")
    # まる 
    else:
        print("예약이 완료되었습니다!")    
# ばちゅ   
else:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")     