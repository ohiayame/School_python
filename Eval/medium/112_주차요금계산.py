# 30분 초과분을 10분 단위로 올림 청구
print("=== 주차 요금 계산기 ===")
enter_time = int(input())  # 입차 시간
exit_time = int(input())   # 출차 시간
parked = exit_time - enter_time # 주차 시간

# 기본 요금: 30분 이하 2000원
base_price = 2000

# 초기화
additional_time = 0
additional_price = 0

# 30분 초과: 10분당 500원(10분 미만의 나머지도 500원 청구)
if parked > 30:
    additional_time = parked - 30
    additional_price = ((additional_time + 9) // 10) * 500

# 총 요금 계산
total = base_price + additional_price

# 결과 값 출력
print(f"주차 시간: {parked}분")
print(f"기본 요금: {base_price}원")
if additional_time:
        print(f"추가 시간: {additional_time}분")
print(f"추가 요금: {additional_price}원")
print(f"총 요금: {total}원")