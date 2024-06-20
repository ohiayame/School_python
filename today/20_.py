import random
# 메뉴 내용 함수
def menu():
    width = 20
    print("-" * width)
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("-" * width)

# 숫자 범위 체크 함수
def TrueNumber(start, end, *li):
    for num in li:
        if not (start <= num <= end) :
            return False
    return True

# 구구단 함수
def gugudan():
    while True:
        print("출력하는 구구단을 아래 형식으로 입력하세요(예: 2, 2~5)")
        input_dan = input()
        dan_li = input_dan.split("~")
        dan_li = [int(dan) for dan in dan_li]
        if TrueNumber(2, 9, *dan_li):
            break
        print("2~9 사이의 값으로 입력하세요")

    start = dan_li[0]
    end = dan_li[-1] if len(dan_li) > 1 else dan_li[0]
    for dan in range(start, end + 1):
        for i in range(1, 10):
            print(f"{dan} * {i} = {dan * i}")
        print()
# 삼각형 함수
def triangle():
    while True:
        print("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)")
        height = int(input())
        if TrueNumber(2,3,height):
            break
        print("2 또는 3을 입력하세요")
    li = []
    h = 0
    for hi in range(1, height + 1):
        h += hi
        print(" " * (height - hi),end="")
        while len(li) < h:
            random_num = random.randint(0,9)
            flag = True
            for i in li:
                if i == random_num:
                    flag = False
                    break
            if flag:
                li.append(random_num)
                print(random_num,end="")
        print()
# 함수 호출 
while True:
    menu()
    input_menu = int(input("원하는 메뉴 번호를 입력하세요: "))
    if input_menu == 1:
        gugudan()
    elif input_menu == 2:
        triangle()
    elif input_menu == 3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~3 사이의 값을 입력하세요")