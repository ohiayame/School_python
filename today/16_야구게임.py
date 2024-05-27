import random

cp_li = []
# 컴퓨터 난수 생성
while len(cp_li) < 3 :
    cp_num = random.randint(0,9)
    num_check = True
    for i in cp_li:
        if i == cp_num:
            num_check = False
    if num_check :
        cp_li.append(cp_num)


game_out = 0
game_count = 0

while True:
    game_count += 1
    # 플레이어 입력
    player_li = list(input(f"시도 {game_count}: 입력한 숫자 - ").split())
    # 결과 출력
    game_strike = 0
    game_ball = 0
    for i in range(3):
        for j in range(3):
            if cp_li[i] == player_li[j]:
                if i == j:
                    game_strike += 1
                else:
                    game_ball += 1
    if game_strike == 0 and  game_ball == 0 :
        game_out += 1
    if game_out > 0:
        print(f"결과{game_strike} Strike, {game_ball} Ball, {game_out} Out")
    else:
        print(f"결과{game_strike} Strike, {game_ball} Ball")  
        
    # 1) 패배 (5번 시도) 2) 패배 (아웃 2번)
    if game_count == 5 or game_out == 2:
        print("게임 종료: 패배", "(시도횟수 5번 초과)"if game_count == 5 else "(2 아웃)")
        break
    
    # 3) 승리 (strike 3)
    elif game_strike == 3:
        print()
        print("게임 종료: 승리")
        break
print("정답:", *cp_li)