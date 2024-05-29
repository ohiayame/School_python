import random
# 컴퓨터가 1부터 100 사이의 숫자를 랜덤하게 선택
random_num = random.randint(1,100)

game_count = 0
# 사용자에게 10번의 기회가 주어짐
while game_count < 10:
    game_count += 1
    # 입력 받기
    input_num = int(input(f"기회 {game_count}/10 - 1부터 100사이의 숫자를 맞춰보세요 (종료하려면 0 입력):"))
    
    # 사용자가 숫자를 맞추면 "정답입니다!"라고 출력되고 0이면 게임이 종료됨.
    if random_num == input_num or input_num == 0:
        print("정답입니다!"if random_num == input_num else "0이 입력되었습니다 ")
        break       
    # 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "더 작은 숫자입니다."라고 출력
    elif input_num > random_num:
        print("더 작은 숫자입니다.")
    # 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "더 큰 숫자입니다."라고 출력
    else:
        print("더 큰 숫자입니다")
    
    # 10번의 시도가 끝날 때까지 숫자를 맞추지 못하면 
    #   -> "모든 기회를 사용하였습니다. 정답은 [숫자]입니다."라고 출력.
    if game_count == 10:
        print(f"모든 기회를 사용하였습니다. 정답은 {random_num}입니다")
print("게임이 끝났습니다")