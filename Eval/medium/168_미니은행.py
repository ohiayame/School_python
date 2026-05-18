# 거래 종류를 판별하여 잔액을 관리하세요.
balance = int(input())

COUNT = 3

for i in range(COUNT):
    # 입력 받기
    data = input().split()

    # 입력 값을 메뉴와 금액으로 나누기
    menu = data[0]
    fee = int(data[1]) if len(data) >= 2 else None

    # 입금의 경우 balance에 추가 후 금액 출력
    if menu == "입금":
        balance += fee
        print(f"입금 완료: 잔액 {balance}원")
    # 출금의 경우 잔액에 따라 결과 값 출력
    elif menu == "출금":
        if balance - fee < 0:
            print("출금 실패: 잔액 부족")
        else:
            balance -= fee
            print(f"출금 완료: 잔액 {balance}원")
    # 이외(조회)의 경우 잔액 출력
    else:
        print(f"현재 잔액: {balance}원")
# 최종 잔액 출력
print(f"최종 잔액: {balance}원")