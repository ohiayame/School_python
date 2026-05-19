# 반복문으로 각 음료 가격을 입력받아 포인트를 누적하세요
order_num = int(input())

# 포인트 적립 변수 선언
total_point = 0

for _ in range(order_num):
    # 가격 입력 받기
    price = int(input())

    # 적립 포인트: 각 음료 가격의 5% (정수 연산으로 부동소수점 오차 방지)
    total_point += price * 5 // 100

# 스탬프: 3잔마다 1개 (총 구매 잔수 // 3)
stamp = order_num // 3

# 결과 값 출력
print(f"총 구매: {order_num}잔")
print(f"총 적립 포인트: {total_point}점")
print(f"스탬프: {stamp}개")