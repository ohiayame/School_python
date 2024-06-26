import random
# 가위바위보 만들기

count_win ,count_lose, count_draw = 0, 0, 0

while True:
    
    # 승리 패배가 2번이상이면 종료
    if count_win >= 2 or count_lose >= 2:
        print("전적:", f"{count_win}승 {count_lose}패 {count_draw}무")
        print("최종 승리: ", "사용자" if count_win ==2 else "컴퓨터")
        break
    
    while True:
    # 사용자로부터 입력 받기
        input_user = input("가위, 바위, 보 중 하나를 입력하세요: ")
        if input_user == "가위" or input_user == "바위" or input_user == "보":
            break
        
        print("가위, 바위, 보 중에서 선택하세요.")
        
    # 컴퓨터 랜덤하게 가위, 바위, 보 중 하나를 선택
    # list만들기
    rsp = ["가위", "바위", "보"]
    input_cp = rsp[random.randint(0, 2)]

    msg_result = ""
    # 결과
    # 1) 무승부
    if input_user == input_cp:
        msg_result = "무승부"
        count_draw += 1
    
    # 2) 승리
    elif input_user == "가위" and input_cp == "보" or \
        input_user == "바위" and input_cp == "가위" or \
        input_user == "보" and input_cp == "바위":
        msg_result = "승리"
        count_win += 1
        
    # 3) 패배
    else:
        msg_result = "패배"
        count_lose += 1
        
    # 출력
    print("사용자: ", input_user, "\n컴퓨터: ", input_cp)
    print(f"{msg_result} 현재전적 : {count_win}승 {count_lose}패 {count_draw}무")
