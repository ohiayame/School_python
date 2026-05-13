# 월을 계절로 변환하세요.
# 입력 값은 1~12라고 가정
month = int(input())

# 초기 값을 "겨울"로 등록 (12월이 해당됨)
season = "겨울"

"""
[조건]
    3, 4, 5월: 봄
    6, 7, 8월: 여름
    9, 10, 11월: 가을
    12, 1, 2월: 겨울
"""
# 조건에 맞게 계절을 저장
# 위의 조건을 통과함에따라 위의 조건 이하의 수는 존재하지 않으로 최대값만 있어도 문재 없음
if month <= 2:
    season = "겨울"
elif month <= 5:
    season = "봄"
elif month <= 8:
    season = "여름"
elif month <= 11:
    season = "가을"

# 결과 값 출력
print(f"{month}월은 {season}입니다.")