import random

# bingo표 표시
def bingoBoard():
    for i in range(len(li)):
        print(li[i], end = " ")
        if (i+1) % n == 0:
            print()

# 랜덤으로 생성한 숫자가 리스트에 있는지 확인
# 있으면 True 
def RandomNum():
    random_num = random.randint(1,16)
    if random_num < 10:
        random_num = " " + str(random_num)
    random_num = str(random_num)
    flag = True
    for i in range(len(li)):
        if li[i] == random_num:
            flag = False
            return random_num, True, i
    if flag:
        return random_num, False, None

# 빙고 표 크기 입력 받기
while True:
    n = int(input("Enter the size of the bingo board (3 to 6): "))
    if 3 <= n <= 6:
        break
    print("Size must be between 3 and 6. Please try again.")
    
# 랜덤 숫자 리스트 생성
li = []
while len(li) < n*n :
    num, flag, i= RandomNum()
    if flag:
        continue
    li.append(num)

# 생성한 bingo표 표시 
print("Initial Bingo Board:")
bingoBoard()

# 게임 시작 
bingo = 0
count = 0
while bingo < 2:
    count += 1
    inp = input("\nPress Enter to generate a random number:")
    find_random, flag, index= RandomNum()
    print(f"Random Number {count}: {find_random}")
    # 같은 숫자가 없으면 다시
    if not flag:
        continue
    # 있으면 *로 변환
    else:
        li[index] = "* "
        bingoBoard()
    # 세로y 가로x bingo 확인
    bingo = 0
    for y in range(n):
        x_star = 0
        y_star = 0
        for x in range(n):
            if li[(n*y)+x] == "* ":
                x_star += 1
                if x_star == n:
                    bingo += 1
            else:
                x_star = 0
            if li[(n*x)+y] == "* ":
                y_star += 1
                if y_star == n:
                    bingo += 1
    # 대각선 bingo 확인
    Rnaname = 0
    Lnaname = 0
    for i in range(n):
        if li[(n*i)+i]== "* ":
            Rnaname += 1
            if Rnaname == n:
                    bingo += 1
        if li[(n*i)+(2-i)]== "* ":
            Lnaname += 1
            if Lnaname == n:
                    bingo += 1
# 결과 출력
print("Congratulations! You've won the game with 2 or more bingos!")