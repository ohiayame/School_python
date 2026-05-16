# 각 감가율을 따로 계산한 뒤 합산하고 최저가를 체크하세요.
new_price = int(input())
year = int(input())
km = float(input())
accident:bool = input().upper() == "Y" # Y 또는 y면 True

# 1. 연식 감가율(%):
# year <= 3: year * 10
if year <= 3:
    year_depreciation_rate = year * 10
# year <= 7: 3*10 + (year-3)*7
elif year <= 7:
    year_depreciation_rate = 3 * 10 + (year - 3) * 7
# year > 7: 3*10 + 4*7 + (year-7)*5
else:
    year_depreciation_rate = 3 * 10 + 4 * 7 + (year - 7) * 5

# 2. 주행거리 감가율(%):
# km <= 5: 0
if km <= 5:
    km_depreciation_rate = 0
# km <= 10: 5
elif km <= 10:
    km_depreciation_rate = 5
# km > 10: 10
else:
    km_depreciation_rate = 10

# 3. 사고 감가율(%): Y 또는 y면 15, 아니면 0.
accident_depreciation_rate = 15 if accident else 0

# 4. 총 감가율 = 세 감가율 합
total_discount = year_depreciation_rate + km_depreciation_rate + accident_depreciation_rate

# 5. 최종 가격 = int(new_price * (1 - total_discount/100))
price = int(new_price * (1 - total_discount / 100))
# 6. 최소 가격 = int(new_price * 0.1)
min_price = int(new_price * 0.1)
# 최종 가격이 최소보다 작으면 최소 가격으로
if price < min_price:
    price = min_price

# 결과 값 출력
print("--- 감가 내역 ---")
print(f"연식 감가 ({year}년): {year_depreciation_rate}%")
print(f"주행거리 감가: {km_depreciation_rate}%")
print(f"사고 감가: {accident_depreciation_rate}%")
print(f"총 감가율: {total_discount}%")
print(f"예상 중고차 가격: {price}만원")