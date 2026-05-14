# AB형을 A보다 먼저 검사해야 합니다.
blood = input()

# 혈액형-성격 맵
personalities = {
    "AB": "이성적이고 독창적인 성격",
    "A": "꼼꼼하고 신중한 성격",
    "B": "자유롭고 창의적인 성격",
    "O": "사교적이고 리더십이 강한 성격",
}

# personalities에서 성격 설명 조회
personality_desc = personalities.get(blood)

# 결과 출력
# 결과 값이 있으면 혈액형과 성격 출력
if personality_desc:
    print(f"혈액형: {blood}형")
    print(f"성격: {personality_desc}")
# 그 외 입력은 잘못된 입력입니다.만 출력
else:
    print("잘못된 입력입니다.")