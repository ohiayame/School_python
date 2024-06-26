import random
# 선언
victory = 0
lose = 0
draw = 0

# 반복문
while True:
    # 리스트 만들기
    li =["가위", "바위", "보"]
    # 사용자로부터 입력 받기
    input_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")
    # 다른 단어 입력받으면 처음부터
    if input_choice != "가위" and input_choice != "바위" and input_choice != "보":
        print("가위, 바위, 보 중에서 선택하세요.")
        print()
        continue
    
    # cp random으로 받고 출력
    # cp_choice = random.choice(li) 
    cp_choice = li[random.randint(0,2)]
    print("컴퓨터: ",cp_choice)
    
    # cp가 바위 때 결과에 따라 증가
    if cp_choice == "바위":
        if input_choice == "바위":
            draw += 1
            msg = "무승부!"
            
        elif input_choice == "가위":
            lose += 1
            msg = "패배" 
        else:
            victory += 1
            msg = "승리!"
    
    # cp가 가위 때 결과에 따라 증가
    elif cp_choice == "가위":
        if input_choice == "바위":
            victory += 1
            msg = "승리!" 
        elif input_choice == "가위":
            draw += 1
            msg = "무승부!" 
        else:
            lose += 1 
            msg = "패배"
    
    # cp가 보 때 결과에 따라 증가
    else:
        if input_choice == "바위":
            lose += 1 
            msg = "패배"
        elif input_choice == "가위":
            victory += 1 
            msg = "승리!"
        else:
            draw += 1
            msg = "무승부!"
    
    # 결과 출력        
    print(f"{msg} 현재 전적: {victory}승 {lose}패 {draw}무")
    print()
    
    # 승리하면 결과출력, break
    if victory >= 2:
        print(f"전적: {victory}승 {lose}패 {draw}무")
        print("최종 승자: 사용자")
        break
    # 패배하면 결과출력, break
    elif lose >= 2:
        print(f"전적: {victory}승 {lose}패 {draw}무")
        print("최종 승자: 컴퓨터")
        break