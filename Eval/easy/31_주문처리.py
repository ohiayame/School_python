# 배달일 때만 거리(int)를 추가로 입력받으세요.
order_type = input()
price = 15000

# 배달이면 거리(km, 정수)를 추가로 입력받고:
if order_type == "배달":
    # 거리 입력 받기
    distance = int(input())
    # 배달비 초기화
    delivery_fee = 0

    # 거리 3km 이하: 배달비 2000원
    if distance <= 3:
        delivery_fee = 2000
    # 거리 3km 초과: 배달비 3500원
    else:
        delivery_fee = 3500
    # 출력: 배달 주문: 음식 15000원 + 배달비 {배달비}원 = 총 {합계}원
    print(f"배달 주문: 음식 {price}원 + 배달비 {delivery_fee}원 = 총 {price + delivery_fee}원")

# 포장이면 2000원 할인:
elif order_type == "포장":
    # 할인 가격 정의
    sale = 2000

    # 출력: 포장 주문: 음식 15000 - 할인 2000원 = 총 13000원
    print(f"포장 주문: 음식 {price}원 - 할인 {sale}원 = 총 {price - sale}원")

# 그 외: 잘못된 주문 방식입니다.
else:
    print("잘못된 주문 방식입니다.")