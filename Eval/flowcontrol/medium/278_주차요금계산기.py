# 바깥 if는 회원/비회원, 안쪽 if는 시간 분기로 작성하세요.
is_member = input() == "True"
hours = int(input())

# 회원이면
if is_member:
    # 1시간 이하: 무료
    # 1시간 초과: 초과 1시간당 1000원 → 요금: XXX원
    if hours <= 1:
        print("무료")  # 조건 분기 안에서 바로 출력해 중복 검사 제거
    else:
        price = (hours - 1) * 1000
        print(f"요금: {price}원")

# 비회원이면
else:
    # 1시간 이하: 요금: 2000원
    # 1시간 초과: 기본 2000원 + 초과 1시간당 2000원 → 요금: XXX원
    price = 2000 + (hours - 1) * 2000  # 요금 구조(기본+초과)를 그대로 표현
    print(f"요금: {price}원")