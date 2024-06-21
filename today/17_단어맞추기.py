# 단어 맞추기 게임
import random
# 1)  세번 단어(5~ 20 길이)를 입력 받고 예외 일 때는 반복
input_li = []
for i in ["첫", "두", "세"]:
    # !!! "()번째 입력 하세요" 라고 출력
    while True:
        input_msg = input()    # 입력 받기
        # !!만약에 5~ 20길이면 input_li에 입력받은 msg를 추가하고 while문에서 탈출
        
        
        # !!5~ 20길이 아니면 "5이상 20이하 글자로 구성된 단어를 입력 하세요."를 출력해서 반복
        
# 2) 렌덤으로 단어를 선택
random_index = # !!! 0~2 의 숫자를 렌덤하게 생성
random_msg = input_li[random_index] # 입력 받은 세개의 단어 중 1개를 선택
print(f"\n단어 선택이 완료 게입을 시작합니다. 선택된 단어: {random_msg}\n")

# 3) 선택한 단어를 blind처리 (올림)
blind = len(random_msg) - len(random_msg) // 2 # 50%를 blind처리 해야됨 (만약에 len(random_msg)가 5면 3개

blind_ = blind # blind처리할때만 사용하는 blind수의 복사본을 생성
blind_li = [i for i in random_msg] # 렌덤하게 선택한 단어를 한 글자씩 리스트에 넣기
# for i in random_msg:
#   blind_li.append(i)

# !!! blind해야 할 개수(blind_)가 0이되면 반복종료 (while문)(1이상이면 실행)

    random_index = random.randint(0, len(random_msg) - 1)  #blind하는 글자를 index을 사용해 렌덤하게 선택  
    # !!!! 만약에 선택한 index의 원소(blind_li[random_index])가 이미처리된 글자("_") 아니면 "_"로 변경
        
        
        #!!! "_"로 변경하면 blind_을 빼기(-1)

# !!!!while문을 시작하기 전에 게임횟수를 세는 변수(game_count)를 선언

# 4) 게임 시작 (다 맞출 때 까지 반복)
while blind > 0:
    # !!!!! 게임횟수 세기 (+1)
    
    print(f"{game_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력 하세요")  # ()번째시도
    print("".join(str(i) for i in blind_li),"\n")   # 현재 blind되어 있는 단어를 문자열로 출력
    input_char = input()  # 알파벳 1개 입력 받기
    
    # 몇개 맞는지 확인 
    count = 0
    li = [i for i in random_msg]
    for i in range(len(random_msg)): # index으로 확인
        # 
        if li[i] == input_char and blind_li[i] == "_": 
            blind_li[i] = input_char
            blind -= 1
            count += 1
    if blind > 0:
        print(f"\n입력한 알파벳 단어 내 포함:{count}글자" if count > 0 else "단어 내 포함되지 않은 알파벳입니다\n")

# 5) 다 맞추면 Clear, 단어와 총 시도횟수를 출력
print(f"\nClear - 선택된 단어: {random_msg}, 총 시도 횟수:{game_count}")