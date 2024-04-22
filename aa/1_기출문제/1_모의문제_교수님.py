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
        while True:
        #print("구구단 출력, 추후 구현")

            # 구구단의 단 입력
            dan = int(input("단을 입력 하세요: "))
            if 2 <= dan <= 9:
                #해당 단위 구구단
                for num in range(1,10):
                    print(dan, "X", num, "=", dan * num)
                break
    # 메뉴 값 == 2
    elif select_menu =='2':
        # 프로그램 종료
        print("프로그램 종료")
        break
    
    # 메뉴 값이 != 1 and 메뉴 값!= 2
    # 에러메시지 출력
    else:
        print("메뉴 값은 1 또는 2만 입력")            
        
        
        
        
# 1~100 사이 정수중 3의 배수와 7의 배수를 출력하시오        
for num in range(1,101):
    if num % 3 == 0 or num % 7 == 0:
        print(num,"\t",end='')
    