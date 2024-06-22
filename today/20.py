import random
# 메뉴 출력함수
def menu():
    width = 20
    print("-" * width)
    print("1. 구구단 출력")
    print("2. 랜덤값  삼각형 출력")
    print("3. 종료")
    print("-" * width)
# 숫자의 범위 확인
def True_num(start, end, *li):
    for i in li:
        if not start <= i <= end:
            return False
    return True

# 구구단 함수
def gugudan():
    while True:
        print("출력할 구구단을 아래 형식으로 입력하세요(예: 2, 2~5)")
        dan = input()
        dan_li = dan.split("~")
        dan_li = [int(d) for d in dan_li]
        if True_num(2,9,*dan_li):
            break
        print("2~9사이의 값을 입력하세요")
    start = dan_li[0]
    end = dan_li[-1] if len(dan_li) > 1 else dan_li[1]
    for d in range(start, end + 1):
        for i in range(1,10):
            print(f"{d} * {i} = {d*i}")
        print()

# 삼각형 함수
def triangle():
    while True:
        print("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)")
        input_num = int(input())
        if True_num(2,3,input_num):
            break
        print("2 또는 3을 입력하세요")
    li = []
    n = 0
    for h in range(1,input_num+1):
        print(" "* (input_num - h),end="")
        n += h
        while len(li) < n:
            randomnum = random.randint(0,9)
            flag= True
            for i in li:
                if i == randomnum:
                    flag = False
                    break
            if flag:
                print(randomnum,end="")
                li.append(randomnum)
        print()
# 출력
while True:
    menu()
    input_menu = int(input("원하는 메뉴 번호를 입력하세요:"))
    if input_menu == 1:
        gugudan()
    elif input_menu == 2:
        triangle()
    elif input_menu == 3:
        print("프로그램 종료")
        break
    else:
        print("1~3 사이의 값을 입력하세요")