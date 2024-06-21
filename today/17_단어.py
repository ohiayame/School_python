# 단어 맞추기
import random
# 1) 5이상 20이하 글자 3단어 입력 받기
# 출력 문장 -> 개행 -> 입력 받기
input_li =[]
for m in ["첫","두", "세"]:
    print(f"{m} 번째 단어를 입력 하세요") 
    while  5 > len(input_msg) > 20:
        input_msg = input()
        if 5 > len(input_msg) > 20:
            print("5이상 20이하 글자로 구성된 단어를 입력 하세요")
    input_li.append(input_msg)

# 2) 개행 -> 랜덤으로 한개 단어를 선택 : 출력 -> 개행
random_msg = random.choice(input_li)
print(f"\n단어 선택 완료 게임을 시작합니다.선택 단어:{random_msg}\n")

# 3) blind 처리 (올림 50%)
b = len(random_msg) - len(random_msg) //2
blind = b
char_li = [char for char in random_msg]
while b > 0:
    index = random.randint(0,len(char_li))
    if char_li[index] != "_":
        char_li[index] = "_"
        b -= 1
# 4) 게임시작
game_count = 0
while blind > 0:
    game_count += 1
    # 1) 시도 횟수 출력
    print(f"{game_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요.")
    # 2) blind 되어 있는 단어를 출력 
    print(*char_li, sep='')
    # 3) 개행 -> 한 글자를 입력 받기 -> 개행
    input_char = 
    # 4) 입력 받은 글자가 몇번 나오는지 확인 -> 출력 (없으면 -> 출력 -> 개행) 
    # 5) blind 다 맞추면 종료
# 5) 결과 출력 (단어랑 시도횟수)
    
