# 7일 초과분에 대해 일당 200원 부과
days = int(input())

price = 0

# 7일 이내: 무료 (0원)
# 8일부터: 일당 200원 추가 (초과 일수 × 200)
if days > 7:
    price += (days - 7) * 200

# 결과 출력
print(f"대여 일수: {days}일")
print(f"대여료: {price}원")