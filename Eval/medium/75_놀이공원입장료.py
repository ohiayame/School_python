# 나이별 요금 결정 후 단체 할인을 판단하세요.
age = int(input())
group_count = int(input())

is_group_sale:bool = group_count >= 10
base_fee = 0

# 기본 입장료:
# age <= 3: 0원
if age <= 3:
    base_fee = 0
# age <= 12: 15000원
elif age <= 12:
    base_fee = 15000
# age <= 18: 20000원
elif age <= 18:
    base_fee = 20000
# age <= 64: 30000원
elif age <= 64:
    base_fee = 30000
# 그 외: 10000원
else:
    base_fee = 10000

price = base_fee
# 그룹 가격 계산
if is_group_sale:
    price = int(base_fee * 0.8)
# 총 금액 계산
total = price * group_count

# 계산한 결과 값 출력
print(f"기본 입장료: {base_fee}원")
# 그룹 할인 적용시만 출력
if is_group_sale:
    print("단체 할인 적용 (20%)!")
    print(f"1인 할인가: {price}원")
print(f"총 입장료: {total}원")