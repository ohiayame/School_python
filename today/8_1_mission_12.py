#  현재 온도(섭씨)를 입력받습니다
Temperature = float(int(input("현재 온도(섭씨)를 입력하세요: ")))

# 30도 이상: 수영
if 30 <= Temperature:
    msg = "수영"
#  20도 이상 30도 미만: 등산
elif 20 <= Temperature:
    msg = "등산"
#  10도 이상 20도 미만: 자전거 타기
elif 10 <= Temperature :
    msg =  "자전거 타기"
#  10도 미만: 스키
else:
    msg =  "스키"
    
print("현재 온도:",Temperature,"도")    
print("추천 활동:", msg)