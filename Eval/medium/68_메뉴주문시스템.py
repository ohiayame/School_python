# 메뉴판 출력 함수
def menu():
    print("--- 메뉴 ---")
    print("1. 아메리카노 (4000원)")
    print("2. 카페라떼 (4500원)")
    print("3. 녹차 (3500원)")
    print("0. 주문 완료")

# while True와 if/elif/break를 사용하세요.
total = 0

while True:
    # 메뉴판 출력
    menu()
    # 주문 받기
    order = int(input())
    
    # order == 1: 아메리카노를 추가했습니다. 출력 후 금액 추가
    if order == 1:
        print("아메리카노를 추가했습니다.")
        total += 4000
    # order == 2: 카페라떼를 추가했습니다. 출력 후 금액 추가
    elif order == 2:
        print("카페라떼를 추가했습니다.")
        total += 4500
    # order == 3: 녹차를 추가했습니다. 출력 후 금액 추가
    elif order == 3:
        print("녹차를 추가했습니다.")
        total += 3500
    # order == 0: 총 주문 금액: {total}원 출력 후 종료
    elif order == 0:
        print(f"총 주문 금액: {total}원")
        break