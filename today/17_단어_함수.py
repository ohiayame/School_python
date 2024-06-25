# 단어맞추기
import random
# 길이 5~20 확인
def inputMsg(msg):
    while True:
        print(f"{msg} 단어를 입력하세요")
        input_msg = input()
        if 5 <= len(input_msg) <= 20:
            break
        else:
            msg = "5이상 20이하 글자로 구성된 "
    return input_msg
# blind처리 함수
def blindMsg(msg):
    global char_li
    while True:
        index = random.randint(0,len(msg)+1)
        if char_li[index] != "_":
            char_li[index] = "_"
            break

# 단어 3개 입려 받기
msg_li = []
for msg in ["첫 번째","두 번째","세 번째"]:
    input_msg = inputMsg(msg)
    msg_li.append(input_msg)

# 3개의 단어중 하나를 선택
choice_msg = msg_li[random.randint(0,2)]
print(f"\n단어 선택 완료 게임을 시작 합니다: {choice_msg}\n")
char_li = [i for i in choice_msg]

# blind할 글자의 게수를 구하기
blind = len(choice_msg) - len(choice_msg)//2

# blind처리 
for i in range(blind):
    blindMsg(choice_msg)
# 게임 시작
play_count = 0
while blind > 0:
    play_count += 1
    print(f"{play_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.\n",*char_li,sep="")
    # 알파벳 입력 받기
    input_char = input("\n")
    # blind해제
    count = 0
    result_li = [i for i in choice_msg]
    for index in range(len(result_li)):
        if char_li[index] == "_" and result_li[index] == input_char:
            char_li[index] = input_char
            count += 1
            blind -= 1
    # 다 맞추면 게임 종료
    if blind > 0:
        print(f"\n입력한 알파벳 단어 내 포함:{count}글자"if count > 0 else "\n단어 내 포함되지 않은 알파벳입니다.\n")
# 결과
print(f"\nClear - 선택된 단어: {choice_msg}, 총 시도 횟수: {play_count}")