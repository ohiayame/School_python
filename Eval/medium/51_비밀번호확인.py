# chance = 3 로 시작, while chance > 0: 입력 → 비교 → 맞으면 break, 틀리면 chance -= 1
# 출력 형식: print("틀렸습니다. 남은 기회:", str(chance) + "번") — 콤마 뒤 공백 포함)
password = "python"
chance = 3

# 기회가 있을 때 반복
while chance > 0:
    # 비밀번호 입력 받기
    input_password = input()

    # 비밀번호가 맞으면 "로그인 성공!"을 출력하고 강제 종료
    if input_password == password:
        print("로그인 성공!")
        break
    # 아니면(틀리면)
    else:
        # 기회 -1 번
        chance -= 1
        # 기회가 없어지면 "계정이 잠겼습니다" 출력
        if chance == 0:
            print("계정이 잠겼습니다")
        # 아니면(기회가 남아있으면) print("틀렸습니다. 남은 기회:", str(chance) + "번")
        else:
            print("틀렸습니다. 남은 기회:", str(chance) + "번")