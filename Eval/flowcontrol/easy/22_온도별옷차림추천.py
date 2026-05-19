# float로 입력받아 구간별 옷차림을 결정하세요.
temperature = float(input())

outfit = ""
# 5도 미만: 패딩, 두꺼운 목도리
if temperature < 5:
    outfit = "패딩, 두꺼운 목도리"
# 5도 이상 10도 미만: 코트, 니트
elif temperature < 10:
    outfit = "코트, 니트"
# 10도 이상 20도 미만: 자켓, 가디건
elif temperature < 20:
    outfit = "자켓, 가디건"
# 20도 이상 28도 미만: 반팔, 얇은 셔츠
elif temperature < 28:
    outfit = "반팔, 얇은 셔츠"
# 28도 이상: 민소매, 반바지
else:
    outfit = "민소매, 반바지"

# 결과 출력
print(f"현재 기온: {temperature}°C")
print(f"추천 옷차림: {outfit}")