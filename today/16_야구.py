# 야구게임
import random
# 1) 랜덤하게 0~9중 세개를 선택
cp_li = list(random.sample(range(10),3))

game_count = 0
game_out = 0
# 2) 게임 시작
while True:
    game_count += 1
    # 3) 플레이어 3개의 숫자를 입력 받기
    input_li = list(map(int,input(f"시도 {game_count}: 입력한 숫자 - ").split()))
    
    game_strike = 0
    game_ball = 0
    # if index값이랑 원소가 같으면 strike 원소만 같으면 ball
    for i in range(3):
        for j in range(3):
            if cp_li[i] == input_li[j] :
                if i == j:
                    game_strike += 1
                else:
                    game_ball += 1
    # strike와 ball가 없으면 out 
    if game_strike == 0 and game_ball == 0 :
        game_out += 1
    
    # 결과)
    print(f"결과: {game_strike} Strike, {game_ball} Ball" if game_out == 0 else f"결과: {game_strike} Strike, {game_ball} Ball, {game_out} Out")
    # 승리 : strike * 3
    if game_strike == 3:
        msg = "승리"
        break
    # 패배 : 게임 실행 횟수 5이상 or 아웃 횟수 2번 이상
    elif game_count == 5 or game_out == 2:
        msg = "패배 (시도 횟수 5회 초과)"  if game_count == 5 else "패배 (아웃 횟수 2회 초과)"
        break

# 게임종료 후 결과 출력
print(f"\n게임 종료: {msg}")
# 정답을 출력
print("정답:", *cp_li)