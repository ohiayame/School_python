import random
msg_li = []

# 3이상 20이하의 msg 입력 받기
while len(msg_li) < 3:
    for i in ["첫", "두", "세"]:
        print(f"{i} 번째 단어를 입력 하세요")
        while True:
            input_msg = input()
            if 3 <= len(input_msg) <= 20:
                msg_li.append(input_msg)
                break
            else:
                print("3이상 20이하 글자로 구성된 단어를 입력 하세요")

# msg를 렌덤하게 선택 charlist를 두게 생성
msg_choice = msg_li[random.randint(0,2)]
print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어: {msg_choice}") 

choice_li = []
blind_li = []
for char in msg_choice:
    choice_li.append(char)
    blind_li.append(char)

# blind하는 변수 두개 생성
blind_value = len(choice_li) - (len(choice_li) // 2)
blind = blind_value
# blind 하기
while blind_value > 0:
    random_num = random.randint(0, len(choice_li) - 1)
    if blind_li[random_num] != "_":
        blind_li[random_num] = "_"
        blind_value -= 1

# 게임 시작 blind가 없어지면 종료
game_count = 0
while blind > 0:
    game_count += 1 # 게임 횟수 세우기
    blind_msg = ""  # blind된 msg를 생성
    for char in blind_li:
        blind_msg += char
        
    # 현재 시도 횟수와 blind된 msg 를 출력하고 1글자 입력 받기
    print(f"{game_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n{blind_msg}")
    input_char = input()
    
    # 입력 받은 글자가 있는지 찾고 세우기
    char_count = 0
    for index in range(len(blind_li)):
        if (blind_li[index] == "_") and (choice_li[index] == input_char):
            blind_li[index] = input_char
            blind -= 1
            char_count += 1
    
    # 게임중이면 입력 받은 알파벳 수 출력
    if blind > 0 :
        print(f"입력한 알파벳 단어 내 포함: {char_count}글자" if char_count > 0 else "단어 내 포함 되지 않은 알파벳 입니다")
print(f"Clear - 선택된 단어: {msg_choice}, 총 시도 횟수: {game_count}")