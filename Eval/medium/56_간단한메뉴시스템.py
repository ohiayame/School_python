# while True 안에서 메뉴를 먼저 출력한 뒤 input()으로 선택을 받으세요.
while True:
    # 메뉴를 출력
    print("===== 메뉴 =====")
    print("1. 인사")
    print("2. 날씨")
    print("q. 종료")
    print("================")

    # 입력 받기
    choice = input()
    # 1 입력 → 안녕하세요! 출력
    if choice == "1":
        print("안녕하세요!")
    # 2 입력 → 오늘 날씨가 좋습니다! 출력
    elif choice == "2":
        print("오늘 날씨가 좋습니다!")
    # q 입력 → 프로그램을 종료합니다를 출력한 후 종료(break)
    elif choice == "q":
        print("프로그램을 종료합니다")
        break
    # 그 외 → 잘못된 입력입니다
    else:
        print("잘못된 입력입니다")