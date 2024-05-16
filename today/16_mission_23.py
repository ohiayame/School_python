# 야구 게임 만들기

import random

game_count = 0
while True :
    
    li = [0,1,2,3,4,5,6,7,8,9]
    cp_choice =  []
    
    strike = 0
    ball = 0
    out = 0
    # 1) 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성

    for i in range(3):
        computer_num = random.choice(li)
        li.remove(computer_num)
        cp_choice.append(computer_num)

    print(cp_choice)
    # 2) 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력
    player_num = list(map(int,input().split()))
    print(player_num)
    
    # 3) 게임 패배
    #    시도 횟수가 5번 이상일 경우, 스트라이크 아웃(Strike out) 횟수가 2번 이상일 경우
    for cp_index in range(3):
        for py_index in range(3):
            if cp_index == py_index:
                # print(type(cp_choice[cp_index]) )
                # print(type(cp_index))
                # print(player_num[py_index])
                
                if cp_choice[cp_index] == player_num[py_index]:
                    strike += 1
            elif cp_choice[cp_index] == player_num[py_index]:
                ball += 1
        
    print(strike, ball) 
    game_count += 1 
    if strike == 3 :
        break
    if game_count == 5:
        break      
    # 4) 게임 승리
    #    플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
