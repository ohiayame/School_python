# N개 상품 가격을 입력받아 조건부 할인 후 총액을 출력하세요.
n = int(input())
total = 0

for _ in range(n):
    price = int(input())
    # 10000원 이상인 상품만 20% 할인을 적용하고,
    if price >= 10000:
        price *= 0.8

    # 10000원 미만 상품은 원래 가격 그대로 합산합니다.
    total += int(price)

# 결과 값 출력
print(f"총액: {total}원")