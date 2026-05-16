# 거리 계산 후 야간 여부를 추가 판단하세요.
distance = float(input())
hour = int(input()) 

base_fee = 4800    # 기본 요금
extra_fee = 0      # 추가 요금
night_fee = 0      # 야간 할증
# 총 금액을 기본요금으로 초기화
total = base_fee

# 2km 초과 시 추가요금
if distance > 2:
    # int((distance - 2) * 1000) 원 정의하고 total에 추가
    extra_fee = int((distance - 2) * 1000)
    total += extra_fee

# 야간 할증(hour >= 22 또는 hour < 6) (총 요금의 20% 추가)
if hour >= 22 or hour < 6:
    # 야간 할증 계산하고 total에 추가
    night_fee = int(total * 0.2)
    total += night_fee

# 계산 결과 출력
print(f"기본요금: {base_fee}원")
print(f"추가요금: {extra_fee}원")
# 야간 할증이 있을 때만 출력
if night_fee:
    print(f"야간 할증 (20%): {night_fee}원")
print(f"총 택시비: {total}원")