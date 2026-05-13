# "예"로 답한 재료만 이어 붙여 "나의 파스타: ..." 형식으로 출력하세요.
add_cheese = input()
add_bacon = input()
add_shrimp = input()
pasta = "파스타"

# add_cheese의 입력 값이 "예"일 경우 pasta에 " + 치즈" 추가
if add_cheese == "예":
    pasta += " + 치즈"

# add_bacon의 입력 값이 "예"일 경우 pasta에 " + 베이컨" 추가
if add_bacon == "예":
    pasta += " + 베이컨"

# add_shrimp의 입력 값이 "예"일 경우 pasta에 " + 새우" 추가
if add_shrimp == "예":
    pasta += " + 새우"

# 결과 값 출력
print(f"나의 파스타: {pasta}")