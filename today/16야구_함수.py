# 야구게임
import random
# 결과 검사 함수
def NumCheck():
    global game_out
    game_strike = 0
    game_ball = 0
    for i in range(3):
        for j in range(3):
            if cp_li[i] == input_li[j]:
                if i == j:
                    game_strike += 1
                else:
                    game_ball += 1
    if game_ball == 0 and game_strike == 0:
        game_out += 1
    return game_strike, game_ball, game_out
    
# 랜덤으로 중복되지 않는 3개 숫자 0~9 생성 (리스트)
cp_li = []  # [random.sample(range(10),3)]
while len(cp_li) < 3:
    random_ = random.randint(0,9)
    flag = True
    for i in cp_li:
        if i == random_:
            flag = False
    if flag:
        cp_li.append(random_)
        
# 게임 시작
game_count = 0
game_out = 0
while True:
    game_count += 1
    # 플레이어) 중복되지 않는 3개 숫자 0~9 입력 받기 *예외 처리 없음 (리스트)
    input_li = list(map(int,input(f"시도 {game_count}: 입력한 숫자 - ").split()))
    
    game_strike, game_ball, game_out = NumCheck()
    # 결과) 
    print(f"결과: {game_strike} Strike, {game_ball} Ball{f", {game_out} Out" if game_out > 0 else ""}")
    
    # 승리) strike 3
    if game_strike == 3:
        msg = "승리"
        break
    # 패배) game_out 2, out 5
    elif game_count == 5 or game_out == 2:
        msg =f"패배 ({f"시도 횟수 {game_count}회 초과" if game_count == 5 else "2 out"})" 
        break
print(f"\n게임 종료: {msg}\n정답:",*cp_li)
