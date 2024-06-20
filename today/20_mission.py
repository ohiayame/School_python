# 메뉴 함수
import random


def menu_print():
    width = 20
    print("-"*width)
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("-"*width)

# 숫자의 범위에 맞는지 확인하는 함수
def TrueNum(start, end, *li):
    for num in li:
        if not (start <= num <= end):
            return False
    return True

# 구구단 함수
def gugudan():
    while True:
        # 구구단의 범위를 입력 받음
        print("출력할 구구단을 아래 형식으로 입력하세요(예: 2, 2~5)")
        input_dan = input()
        dan_li = input_dan.split("~")
        dan_li = [int(dan) for dan in dan_li]
        # 함수를 호출해서 예외처리
        if TrueNum(2, 9, *dan_li):
            break
        print("2~9 정수를 입력 하세요")
    # 2, 2~9 입력에 따라 결과를 출력
    start = dan_li[0]
    end = dan_li[1] if len(dan_li) > 1 else dan_li[0]
    for dan in range(start, end + 1):
        for i in range(1,10):
            print(f"{dan} * {i} = {dan* i}")
    # 단마다 개행
    print()

# 삼각형 함수
def triangle():
    while True:
        # 삼각형의 높이를 입력 받음
        print("삼각형의 노ㅍ이 줄 수를 입력하세요(2 이상 3이하)")
        input_height = int(input())
        # 함수를 호출해서 예외처리
        if TrueNum(2, 3, input_height):
            break
        print("2 또는 3을 입력하세요")
    
    li = []
    h = 0
    for j in range(1,input_height+1):
        # 공백을 출력
        print(" " * (input_height - j),end="")
        # 숫자를 출력
        h += j
        while len(li) < h:
            # 랜덤으로 숫자를 생성
            random_ = random.randint(0,9)
            # 중복이 없는지 리스트로 확인
            flag = True
            for i in li:
                if i == random_:
                    flag = False
                    break
            if flag:
                li.append(random_)
                print(li[-1],end="")
        # 개행을 출력
        print()
# 반복
while True:
    menu_print()
    # 메뉴를 입력 받기
    input_menu = int(input("원하는 메뉴 번호를 입력하세요: "))
    # 만약에 1이면 구구단 함수 호출
    if input_menu == 1:
        gugudan()
    # 2면 삼각형(랜덤 값) 함수 호출
    elif input_menu == 2:
        triangle()
    # 3이면 반복 종료
    elif input_menu == 3:
        break
    # 예외 처리
    else:
        print("1~3 사이의 값을 입력하세요")