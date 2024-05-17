# 야구 게임 만들기

import random
# 게임 카운트를 선언
game_count = 0

# pc 가 고르는 번호 리스트를 제시  , 선택한 번호를 넣는 리스트도 샌선  
#li = [0,1,2,3,4,5,6,7,8,9]
cp_choice =  []

# out count 선언
out = 0

# 1) 게임 시작 시 0~9 사이의 중복되지 않는 정수 3개를 생성
# 리스트에서 하나 걸라서 빼서 choice리스트에 넣기
    # for i in range(3):
    #     computer_num = random.choice(li)
    #     li.remove(computer_num)
    #     cp_choice.append(computer_num)
while len(cp_choice) < 3:
    computer_num = random.randint(0,9)
    flag = True
    for num in cp_choice:
        if num == computer_num:
            flag = False
    if flag:
        cp_choice.append(computer_num)
        
    # num_range = range(10)
    # cp_choice = random.sample(num_range, 3)

# 게임 반복 시작
while True:
    # 2) 플레이어는 키보드를 통해 0~9 사이의 정수 3개를 입력
    player_num = list(map(int,input(f"시도 {game_count}: 숫자를 입력 하세요").split()))

    
    
    strike = 0
    ball = 0
    
    # 3) 게임 패배
    #    시도 횟수가 5번 이상일 경우, 스트라이크 아웃(Strike out) 횟수가 2번 이상일 경우
    for cp_index in range(3):
        for py_index in range(3):
            if cp_index == py_index:                
                if cp_choice[cp_index] == player_num[py_index]:
                    strike += 1
                    
            elif cp_choice[cp_index] == player_num[py_index]:
                ball += 1
    
    if strike == 0 and ball == 0:
        out += 1
        
        
    game_count += 1 
    
    if out >= 1:
        print(f"결과: {strike} Strike, {ball} Ball, {out} Out")
    else:
        print(f"결과: {strike} Strike, {ball} Ball")
    
    if game_count == 5:
        msg = "패배 (시도횟수 5회 초과)"
        break
    elif out == 2:
        msg = "패배 (Strike out 횟수 2번 초과)"
        break
        
    
    # 4) 게임 승리
    #    플레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 모두 맞출 경우
    elif strike == 3  :
        msg = "승리"
        break
print("게임 종료:", msg)

# re_num = ""
# for i in cp_choice:
#     re_num += str(i) + " "
# print("정답", re_num)

print(f"정답: {" ".join(map(str,cp_choice))}")