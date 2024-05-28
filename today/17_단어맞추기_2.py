import random

# 1) 단어 입력 3개 5이상 20이하 else 재입력
msg_li = []
for m in ["첫", "두", "세"]:
    print(f"{m} 번째 단어를 입력 하세요")
    while True:
        input_msg = input()
        if 3 <= len(input_msg) <= 20:
            msg_li.append(input_msg)
            break
        else:
            print("3이상 20이하 글자로 구성된 단어를 입력 하세요")

# 2) 렌덤으로 단어 선택 
random_msg = msg_li[random.randint(0,2)]
print(f"\n단어 선택 완료 게임을 시작합니다. 선택된 단어: {random_msg}\n")

# blind 하는 list와 그대로 유지하는 리스트를 생성 
randomchar_li = list(random_msg)
blind_li = randomchar_li[:]

# 3) 단어의 50%를 blind 
blind_value = len(blind_li) - len(blind_li) // 2

# 렌덤으로 생성된 index값의 blind리스트의 원소가 _ 아니면 대입
blind = blind_value
while blind_value > 0:
    index = random.randint(0, len(blind_li)- 1)
    if blind_li[index] != "_":
        blind_li[index] = "_"
        blind_value -= 1

# 게임시작 blind가 없어지면 종료
game_count = 0
while blind > 0:
    game_count += 1     # 게임 횟수 세우기
    blind_msg = ""      # blind된 msg를 생성
    for char in blind_li:
        blind_msg += char
    
    # 4) char 입력 받기
    print(f"{game_count}번째 시도, 아래 단어를 구성하는 알파벳을 입력하세요\n{blind_msg}\n")
    input_char = input()
    
    # 5) 맞으면 blinde해제
    char_count = 0
    for i in range(len(blind_li)):
        if input_char == randomchar_li[i] and blind_li[i] == "_":
            blind_li[i] = input_char
            blind -= 1
            char_count += 1
    
    # 6) 다 맞추면 게임 종료
    if blind > 0:
        print(f"\n입력한 알파벳 단어 내 포함: {char_count}글자" if char_count > 0 else "단어 내 포함되지 않은 알파벳입니다\n")

# 7) 결과 출력
print(f"Clear - 선택된 단어: {random_msg}, 총 시도 횟수: {game_count}")