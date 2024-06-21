# 야구게임
import random
# 1)랜덤으로 컴퓨터 난수 생성 (0~9, 3개 리스트)
cp_li = []
while len(cp_li) < 3:
    random_num = random.randint(0, 9)
    flag = True
    for i in cp_li:
        if i == random_num:
            flag = False
    if flag:
        cp_li.append(random_num)
game_count = 0
game_out = 0
# 게임 시작
while True:
    # 게임 시도 횟수
    game_count += 1
    # 2) 입력 받기 (0~9, 3개 리스트)
    input_li = list(map(int,input(f"시도 {game_count}: 입력한 숫자 - ").split()))
    game_strike = 0
    game_ball = 0
    for i in range(3):
        for j in range(3):
            if cp_li[i] == input_li[j]:
                if i == j:
                    game_strike += 1
                else:
                    game_ball += 1
    if game_strike == 0 and game_ball == 0:
        game_out += 1
        
    # 게임 결과 출력 (아웃이 있으면 출력
    print(f"{game_strike} Strike, {game_ball} Ball{"" if game_out == 0 else f", {game_out} Out"}")
    # 게임 패배 조건 , 시도 횟수가 5번 이상 , Strike out 횟수가 2번 이상
    if game_count == 5 or game_out == 2:
        print(f"게임 종료: 패배 {"(시도 횟수 5회 초과)"if game_count == 5 else "(2 아웃)"}")
        break
    # 게임 승리 조건, STRIKE 3개
    if game_strike == 3:
        print("게임 종료: 승리")
        break
# 게임종료 후 결과 출력
# 정답 출력
print("정답:", *cp_li)