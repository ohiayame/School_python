# 잔액이 가격보다 적으면 "잔액이 부족합니다"를 출력하세요.
price = int(input())
balance = int(input())

# 커피 가격이 내 잔액 보다 비싸면 "잔액이 부족합니다" 출력
# if price > balance:
if balance < price:
    print("잔액이 부족합니다")

# 잔액이 충분하면 출력 없음