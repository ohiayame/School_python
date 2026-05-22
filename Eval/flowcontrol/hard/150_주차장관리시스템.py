def menu_print():
    print("===== 주차장 관리 =====")
    print("1. 입차")
    print("2. 출차")
    print("3. 현황 조회")
    print("4. 종료")


# while True와 if/elif로 구현하세요.
parked = 0
max_cars = 10
total_income = 0
rate = 1000

while True:
    menu_print()
    menu = int(input())

    # 입차(1): 
    if menu == 1:
        # 만차면 주차장이 만차입니다!
        if parked == max_cars:
            print("주차장이 만차입니다!")
        # 아니면 차량이 입차되었습니다. (현재 주차: K/10대)
        else:
            parked += 1
            print(f"차량이 입차되었습니다. (현재 주차: {parked}/{max_cars}대)")
    # 출차(2): 
    elif menu == 2:
        # 주차된 차 없으면 : 주차된 차량이 없습니다.
        if parked == 0:
            print("주차된 차량이 없습니다.")
        # 있으면
        else: 
            # 시간 입력
            hours = int(input())
            # 요금 = max(0, 시간)*1000
            fee =  max(0, hours) * rate
            total_income += fee
            parked -= 1
            # 주차 요금: F원
            print(f"주차 요금: {fee}원")
            # 차량이 출차되었습니다. (현재 주차: K/10대) / (총 수입 누적)
            print(f"차량이 출차되었습니다. (현재 주차: {parked}/{max_cars}대)")
    # 조회(3): 
    elif menu == 3:
        # 현재 주차: K/10대, 빈 자리: M대, 총 수입: T원
        print(f"현재 주차: {parked}/{max_cars}대")
        print(f"빈 자리: {max_cars - parked}대")
        print(f"총 수입: {total_income}원")
    # 종료(4): 
    elif menu == 4:
        # 시스템을 종료합니다. 출력 후 종료
        print("시스템을 종료합니다.")
        break
    # 그 외: 
    else:
        # 잘못된 메뉴입니다.
        print("잘못된 메뉴입니다.")

    print()