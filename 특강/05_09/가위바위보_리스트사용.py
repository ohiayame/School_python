import random

victory = 0
lose = 0
draw = 0

while True:
    li = ["바위", "가위", "보"]
    li2 = [["무승부!","승리!","패배"],["패배","무승부!","승리!"],["승리!","패배","무승부!"]]

    input_choice = input("my: ")
    
    if input_choice != "가위" and input_choice != "바위" and input_choice != "보":
        print("가위, 바위, 보 중에서 선택하세요.")
        print()
        continue
    
    cp_choice = random.choice(li)
    print("cp:",cp_choice)
    
    myindex = li.index(input_choice)
    cpindex = li.index(cp_choice)
    result = li2[myindex][cpindex]

    if result == "승리!":
        victory += 1
        msg = "승리!"
    elif result == "패배":
        lose += 1
        msg = "패배"
    else:
        draw += 1
        msg = "무승부!"
        
    if victory >= 2 or lose >= 2:
        print("전적:", f"{victory}승 {lose}패 {draw}무")
        print("최종 승리: ", "사용자" if victory ==2 else "컴퓨터")
        break
    
    print(f"{msg} 현재 전적: {victory}승 {lose}패 {draw}무")
    print()