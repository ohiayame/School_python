import random

random_li = []
# 렌덤 숫자 3개
while len(random_li) < 3:
    random_num = random.randint(0,9)
    numflag = True
    for num in random_li:
        if num == random_num:
            numflag = False
    if numflag:
        random_li.append(random_num)

game_out = 0
game_count = 0
while game_count < 5:
    game_count += 1
    # 입력 수사 3개
    input_li = list(map(int,input(f"시도 {game_count}:입력하 숫자 - ").split()))
    game_strike = 0
    game_ball = 0 
    for i in range(3):
        for j in range(3):
            if input_li[i] == random_li[j]:
                if i == j:
                    game_strike += 1
                else :
                    game_ball += 1
    if game_ball == 0 and game_strike == 0:
        game_out += 1
    print(f"결과: {game_strike} Strike, {game_ball} Ball" if game_ball == 0 else f"결과: {game_strike} Strike, {game_ball} Ball, {game_out} Out")
    if game_strike == 3:
        msg = "승리"
        break
    elif game_count == 5 or game_out == 2:
        msg = "페배 (시도 횟수 5번 초과)"if game_count == 5 else "페배 (out 2번)"
        break
print(f"게임 종료:{msg}\n정답:{" ".join(map(str(random_li)))}")