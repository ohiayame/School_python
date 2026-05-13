# 1~7 외의 입력은 else로 처리하세요.
day = int(input())

# 입력에 따른 요일의 맵을 정의
day_map = {
    1: "월요일",
    2: "화요일",
    3: "수요일",
    4: "목요일",
    5: "금요일",
    6: "토요일",
    7: "일요일"
}
# 맵에서 해당 요일 가져오기
result_day = day_map.get(day)

# 결과 출력
# day_map에 존재하는 입력인 경우
if result_day:
    print(f"{day} → {result_day}")
# 아니면 "잘못된 입력입니다."만 출력
else:
    print("잘못된 입력입니다.")