# while True 안에서 guess 입력, tries += 1, 비교/break
answer = 42
tries = 0
print("=== 숫자 맞추기 게임 (1~100) ===")

while True:
    # 입력을 받고 tries +1
    guess = int(input())
    tries += 1

    # 정답을 맞추면 정답입니다! 시도 횟수: {tries}번 출력하고 종료
    if guess == answer:
        print(f"정답입니다! 시도 횟수: {tries}번")
        break
    # 입력값이 정답보다 작으면 UP!
    elif guess < answer:
        print("UP!")
    # 입력값이 정답보다 크면 DOWN!
    else:
        print("DOWN!")