# 입력
departure_time_hour = int(input())   # 출발 시간(시)

departure_time_minute = int(input())  # 출발 시간(분)

time_of_arrival_hour = int(input())   # 도착 시간(시)
time_of_arrival_minute = int(input())   # 도착 시간(분)

# 이동 거리(km)
distance = float(int(input()))

# 총 이동 시간
hour = time_of_arrival_hour - departure_time_hour
minute =  time_of_arrival_minute - departure_time_minute 
# if minute >= 60:
#     minute -= 60
#     hour += 1

# 평균 속도 = 이동 거리(km) / 총 이동 시간(h)
average_speed = distance /  (hour + minute / 60) 
# 이동 시간은 분 단위

# 60km/h 미만 :  "느림"
if average_speed < 60 :
    msg = "느림"
# 60km/h 이상 90km/h 미만: "보통"
elif average_speed < 90 :
    msg = "보통"
# 90km/h 이상 : "빠름"
else:
    msg = "빠름"



# 출력
# 이동 거리: km
print("출력 이동 거리:", distance, "km")
# 출발 시간 : 시 분
print("출발 시간:", departure_time_hour, "시",departure_time_minute, "분")
# 도착 시간 : 시 분
print("도착 시간:", time_of_arrival_hour, "시", time_of_arrival_minute, "분")
# 평균 속도(km/h)
print("평균 속도(km/h):", round(average_speed,2),"km/h")
# 속도 상태
print("속도 상태:", msg)



