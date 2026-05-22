def menu_print():
    print('===== ATM =====')
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액조회")
    print("4. 종료")


# while True와 if/elif로 메뉴 분기를 구현하세요.
balance = 100000
withdraw_limit = 500000
limit_count = 0

while True:
    # menu출력 후 입력 받기
    menu_print()
    order = int(input())

    # 입금(1): 금액 입력 
    if order == 1:
        input_krw = int(input())

        # 양수면 금액원이 입금되었습니다.와 현재 잔액: X원 출력
        if input_krw > 0:
            balance += input_krw
            print(f"{input_krw}원이 입금되었습니다.")
            print(f"현재 잔액: {balance}원")
        # 아니면 입금액은 양수여야 합니다.
        else:
            print("입금액은 양수여야 합니다.")

    # 출금(2): 금액 입력 
    elif order == 2:
        input_krw = int(input())
        # 1. 양수가 아니면 출금액은 양수여야 합니다.
        if input_krw <= 0:
            print("출금액은 양수여야 합니다.")
        # 2. 한도 초과면 1회 출금 한도(500000원)를 초과했습니다.
        elif input_krw > withdraw_limit:
            limit_count += 1
            print(f"{limit_count}회 출금 한도({withdraw_limit}원)를 초과했습니다.")
        # 3. 잔액 부족이면 잔액이 부족합니다. 현재 잔액: X원
        elif input_krw > balance:
            print(f"잔액이 부족합니다. 현재 잔액: {balance}원")
        # 4. 성공이면 금액원이 출금되었습니다.와 현재 잔액: X원
        else:
            balance -= input_krw
            print(f"{input_krw}원이 출금되었습니다.")
            print(f"현재 잔액: {balance}원")

    # 조회(3): 현재 잔액: X원
    elif order == 3:
        print(f"현재 잔액: {balance}원")

    # 종료(4): 이용해 주셔서 감사합니다. 출력 후 종료
    elif order == 4:
        print("이용해 주셔서 감사합니다.")
        break

    # 그 외: 잘못된 메뉴입니다. 다시 선택해 주세요.
    else:
        print("잘못된 메뉴입니다. 다시 선택해 주세요.")

    print()