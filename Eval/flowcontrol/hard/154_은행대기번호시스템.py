def menu_print():
    print("===== 은행 대기번호 =====")
    print("1. 번호 발급")
    print("2. 다음 고객 호출")
    print("3. 대기인원 확인")
    print("4. 종료")

# while True, if/elif로 구현하세요.
last_issued = 0
last_called = 0

while True:
    menu_print()

    menu = int(input())
    wait = last_issued - last_called # 대기 인원 계산

    # 발급(1): 
    if menu == 1:
        # last_issued += 1 → 대기번호 X번이 발급되었습니다.
        last_issued += 1 
        print(f"대기번호 {last_issued}번이 발급되었습니다.")

    # 호출(2): 
    elif menu == 2:
        # 대기 인원 <= 0이면 대기 중인 고객이 없습니다., 
        if wait <= 0:
            print("대기 중인 고객이 없습니다.")
        # 아니면 last_called += 1 → X번 고객님, 오세요!
        else:
            last_called += 1
            print(f"{last_called}번 고객님, 오세요!")

    # 확인(3): 
    elif menu == 3:
        # 현재 대기인원: N명 출력
        print(f"현재 대기인원: {wait}명")

    # 종료(4):
    elif menu == 4:
        # 시스템을 종료합니다. 출력 후 종료
        print("시스템을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다.")

    # 빈 줄 하나 출력  
    print()