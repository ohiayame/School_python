def menu_print():
    print("===== 도서관 대출 시스템 =====")
    print("1. 대출")
    print("2. 반납")
    print("3. 대출현황 조회")
    print("4. 종료")


# while True와 if/elif로 구현하세요.
borrowed = 0
max_books = 5

while True:
    # 메뉴 출력 후 입력 받기
    menu_print()
    menu = int(input())

    # 대출(1):
    if menu == 1:
        # 권수 입력
        books_count = int(input())
        
        # 1. 0 이하면 1권 이상 입력해 주세요.
        if books_count <= 0:
            print("1권 이상 입력해 주세요.")
        # 2. 한도 초과면 대출 한도 초과! 추가 대출 가능 권수: N권
        elif borrowed + books_count > max_books:
            print(f"대출 한도 초과! 추가 대출 가능 권수: {max_books - borrowed}권")
        # 3. 성공이면 X권을 대출했습니다. (현재 대출: Y권)
        else:
           borrowed += books_count
           print(f"{books_count}권을 대출했습니다. (현재 대출: {borrowed}권)") 
    
    # 반납(2): 
    elif menu == 2:
        # 현재 대출이 0이면 현재 대출한 도서가 없습니다.
        if borrowed == 0:
            print("현재 대출한 도서가 없습니다.")
        # 아니면 
        else:
            # 권수 입력 
            books_count = int(input())
            
            # 1. 0 이하면 1권 이상 입력해 주세요.
            if books_count <= 0:
                print("1권 이상 입력해 주세요.")
            # 2. 대출보다 많으면 대출 권수보다 많이 반납할 수 없습니다. (현재 대출: Y권)
            elif books_count > borrowed:
                print(f"대출 권수보다 많이 반납할 수 없습니다. (현재 대출: {borrowed}권)")
            # 3. 성공이면 X권을 반납했습니다. (현재 대출: Y권)
            else:
                borrowed -= books_count
                print(f"{books_count}권을 반납했습니다. (현재 대출: {borrowed}권)")
    
    # 조회(3): 
    elif menu == 3:
        # 현재 대출 권수: X권 / 추가 대출 가능: N권
        print(f"현재 대출 권수: {borrowed}권")
        print(f"추가 대출 가능: {max_books - borrowed}권")

    # 종료(4): 
    elif menu == 4:
        # 이용해 주셔서 감사합니다. 출력 후 종료
        print("이용해 주셔서 감사합니다.")
        break

    # 그 외: 
    else:
        # 잘못된 메뉴입니다. 다시 선택해 주세요.
        print("잘못된 메뉴입니다. 다시 선택해 주세요.")
    print()