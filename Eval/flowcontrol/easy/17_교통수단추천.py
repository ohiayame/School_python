# float로 입력받아 구간별로 판정하세요.
distance = float(input())

"""
[조건]
2km 미만: 도보
2km 이상 5km 미만: 자전거
5km 이상 20km 미만: 버스
20km 이상: 지하철
"""
# 초기값을 "지하철"로 정의
result = "지하철"

# 조건에 맞춰서 추천 교통수단을 선택
if distance < 2.0: 
    result = "도보"
elif distance < 5.0:
    result = "자전거"
elif distance < 20.0:
    result = "버스"

# 결과 출력
print(f"거리: {distance}km")
print(f"추천 교통수단: {result}")