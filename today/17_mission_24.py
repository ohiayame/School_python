import random

# 1) 단어 입력받기
msg_list = []

# 글자  범위는 5 이상, 20 이하 함수
def inputmessage(msg):
    while True:
        print(f"{msg}단어를 입력하세요")
        input_msg = input()
        if 5 <= len(input_msg) <= 20:
            break
        else:
            msg = "5이상, 20이하 글자로 구성된 "
    return input_msg

# 키보드로부터 영어 단어 3개를 입력 받아 리스트에 저장
for msg in ["첫 번째", "두 번째", "세 번째"]:
    input_msg = inputmessage(msg)
    msg_list.append(input_msg)


# 2) 입력된 3개의 단어 중 한 개의 단어를 임의로 선택
try:
    choice_msg = input()
    flag = True
    for i in msg_list:
        if i == choice_msg:
            cerect_msg = choice_msg
            flag = False
    if flag:
        raise ValueError
# 입력이 없으면 random으로 정하기
except Exception:
    index_num = random.randint(0,2)
    cerect_msg = msg_list[index_num]
print("단어 선택 완료 게임을 시작합니다. 선택된 단어:", cerect_msg)
print()

# 선택한 단어를 리스트화
blind_num = 0
char_li = []
for char in cerect_msg:
    char_li.append(char)

# 선택된 단어의 글자 중 50%를  랜덤하게 Blind
blind_num = int( len(cerect_msg) - (len(cerect_msg) // 2) )

# random으로 중복되지 않는 index를 선택-> blind
# blind 횟수를 check 
check_num = 0
while check_num < blind_num:
    randomindex = random.randint(0,len(cerect_msg) - 1)
    index_flag = True
    if char_li[randomindex] == "_":
        index_flag = False
            
    if index_flag:
        char_li[randomindex] = "_"
        check_num += 1


game_count = 0
# 3) 게임시작
while True:
    # 시도 회수
    game_count += 1
    print(f"{game_count}번재 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    
    # blind cerect_msg를 출력
    blind_msg = ""
    for m in char_li:
        blind_msg += m
    print(blind_msg)
    print()
    
    # 키보드로부터 알파벳 한 글자를 입력받기
    input_blind = input()
    print()
    
    index_count = -1
    check = 0   # 몇개 있는지
    Errorflag = True
    
    # 단어의 char랑 입력받은 char가 같으며 _인 경우 Blind를 해제
    for i in cerect_msg:
        index_count += 1
        if i == input_blind and char_li[index_count] == "_":
            char_li[index_count] = input_blind
            check += 1
            blind_num -= 1
            Errorflag = False
    # # 단어의 모든 글자를 맞출 경우 게임이 종료 
    if blind_num == 0:
        break
    # 존재하지 않을 경우 “없음” 메시지를 출력
    if Errorflag:
        print("단어 내 포함되지 않은 알파벳입니다.")
        print()
    else:
        print(f"입력한 알파벳  단어 내 포함: {check}글자")

# 단어,횟수 출력
print(f"Clear - 선택된 단어: {cerect_msg}, 총 시도 회수:{game_count}")