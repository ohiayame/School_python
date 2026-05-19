# 기본료에 무게 추가, 거리 추가를 더하세요
weight = int(input())
dist = int(input())

# 기본료: 3000원
base_price = 3000
add_price = 0

# 무게 추가:
# 2kg 이하: 추가 없음
# 2kg 초과 ~ 10kg 이하: 1000원 추가
if 2 < weight <= 10:
    add_price += 1000
# 10kg 초과: 3000원 추가
elif weight > 10:
    add_price += 3000

# 거리 추가:
# 50km 이하: 추가 없음
# 50km 초과 ~ 100km 이하: 1500원 추가
if 50 <= dist <= 100:
    add_price += 1500
# 100km 초과: 3000원 추가
elif dist > 100:
    add_price += 3000

# 택배 요금 계산
total = base_price + add_price

# 결과 값 출력
print(f"무게: {weight}kg | 거리: {dist}km")
print(f"택배 요금: {total}원")