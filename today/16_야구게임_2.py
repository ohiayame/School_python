import random

cp_li = []
# 1) 컴퓨터가 0~9 3개를 생성
while len(cp_li) < 3:
    cp_random = random.randint(0,9)
    random_flag = True
    for i in cp_li:                 
        if i == cp_random:
            random_flag = False
if random_flag:
        cp_li.append(cp_random)

game_count = 0
game_out = 0
# 게임 시작
while True:
    game_count += 1   # 플래이 횟수 세우기
    # 2) 사용자 0~9 3개를 입력받기 예외 X
    input_li = list(map(int,input(f"시도 {game_count}: 입력한 숫자 - ").split()))
    
    game_strike = 0
    game_ball = 0
    for i in range(len(cp_li)):
        for j in range(len(input_li)):
            if cp_li[i] == input_li[j]:
                if i == j:
                    game_strike += 1    # index와 원소가 같으면 strike
                else:
                    game_ball += 1  # 원소만 같으면 ball   
    # strike도 ball도 없으면 out
    if game_strike == 0 and game_ball == 0:
        game_out += 1
    
    # 결과 
    print(f"{game_strike} Strike, {game_ball} Ball"if game_out == 0 else f"{game_strike} Strike, {game_ball} Ball, {game_out} Out")
    # 패배
    # 시도 횟수 5번이상   or   아웃 2번 이상
    if game_count == 5 or game_out == 2:
        msg = "(시도 횟수 5회 초과)"if game_count == 5 else "(2 아웃)"
        print("게임 종료: 패배", msg)
        break
    # 승리
    # strike 3
    if game_strike == 3:
        print("게임 종료: 승리")
        break
print("정답:", *cp_li)