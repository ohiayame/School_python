while True:
    # 메뉴출력
    print("-" * 10)
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("-" * 10)
    
    # 메뉴 값 입력
    select_menu = input()
    
    # 메뉴값 == 1
    if select_menu == '1':
        print("구구단 출력, 추후 구현")
        
        # 구구단의 단 입력
        dan = int(input())
        #해당 단위 구구단
        for num in range(1,10):
            print(dan,"X",num, "=", dan * num)
            
    # 메뉴 값 == 2
    elif select_menu =='2':
        # 프로그램 종료
        print("프로그램 종료")
        break
    
    # 메뉴 값이 != 1 and 메뉴 값!= 2
    # 에러메시지 출력
    else:
        print("메뉴 값은 1 또는 2만 입력")            