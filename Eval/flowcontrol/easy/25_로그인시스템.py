# 중첩 if문으로 아이디를 먼저, 그 안에서 비밀번호를 확인하세요.
user_id = input()
password = input()

# 아이디가 "admin"이면 비밀번호 정답 여부를 출력
if user_id == "admin":
    if password == "1234":
        print("로그인 성공!")
    else:
        print("비밀번호가 틀렸습니다.")
# 아니면 "ID가 존재하지 않습니다."를 출력
else:
    print("ID가 존재하지 않습니다.")