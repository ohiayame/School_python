# 사이즈별 단가를 정하고, 3판 이상이면 10% 할인
size = input()
qty = int(input())
base_price = 0

# S: 8000원
if size == "S":
    base_price = 8000
# M: 12000원
elif size == "M":
    base_price = 12000
# (S/M/L)중에 입력이 된다고 가정
# L: 15000원
else:
    base_price = 15000

# 금액 계산
total = base_price * qty

# 결과 출력
print(f"사이즈: {size} | 수량: {qty}판")
# 3판 이상 주문 시 총액에서 10% 할인
if qty >= 3:
    total *= 0.9
    print(f"총액: {int(total)}원")
    print("(10% 할인 적용)")
else:
    print(f"총액: {total}원")