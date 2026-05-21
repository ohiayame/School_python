# tuple도 list처럼 `in` 연산자로 멤버십을 검사할 수 있습니다.
menu = ("Espresso", "Latte", "Cappuccino", "Americano")
order = input()

# in 연산자로 멤버십을 검사
if order in menu:
    print("주문 가능")
else:
    print("주문 불가")