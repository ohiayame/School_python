import random 

# 구구단 입력 함수
def gugu_chack(num):
    # ~가 있으면 빼고 a, b에 나눠서 함수 호출
    for i in num:
        if i == "~":
            num_a, num_b = map(int,num.split("~"))
            if 2 <= num_a <= 9 and 2 <= num_b <= 9:
                gugudan(num_a,num_b)
                return True
            else:
                return False
    # 만약에 입력 받은 숫자가 한개면 그냥 함수 호출
    if 2 <= int(num) <= 9:
        gugudan(int(num))
        return True
    # 만약에 2~9사이 값이 아니면 다시 입력 받기
    else:
        return False

# 구구단 출력 함수
def gugudan(num_a, num_b=None):
    # 만약에 받은 숫자가 한개면 a==b
    if num_b == None:
        num_b = num_a
    # for문으로 구구단 출력
    for i in range(num_a, num_b + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        if num_a != num_b:
            print()

# 삼각형 함수
def triangle(value):
    # 높이가 안맞으면 바이바이
    if 2 > value > 3:
        return False
    # 중복을 확인하는 리스트
    li = []
    MSG = ""
    # 중복되지 않는 숫자를 랜덤으로 높이에 맞게 생성
    for i in range(1, value + 1):
        for _ in range(value - i):  # 공백의 수는 높이 -1
            MSG += " " 
        while len(MSG) < value:
            random_ = random.randint(0,9)
            flag = True
            for c in li:
                if c == random_:
                    flag = False
                    break
            if flag:
                MSG += str(random_)
                li.append(random_)
        print(MSG)
        MSG = ""
    return True

# 메뉴를 출력
def menu():
    width = 20
    print("-" * width)
    print("1. 구구단 출력")
    print("2. 랜덤값 삼각형 출력")
    print("3. 종료")
    print("-" * width)

while True:
    # 메뉴를 출력
    menu()
    
    # 메뉴를 입력 받기 
    input_menu = (int(input("원하는 메뉴 번호를 입력하세요: ")))
    
    # 1) 구구단 입력
    if input_menu == 1:
        while True:
            print("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)")
            flag = gugu_chack(input())
            if flag:
                break
            # 예외 처리
            print("2~9 사이의 값으로 입력하세요")
        
    # 2) 랜덤 값 삼각형 입력 2 OR 3
    elif input_menu == 2:
        while True:
            flag = triangle(int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3이하)")))
            if flag:
                break
            # 예외 처리
            print("2 또는 3을 입력하세요")

    # 3) 프로그램 종료 
    elif input_menu == 3:
        print("프로그램을 종료합니다.")
        break
        
    # 예외 처리
    else:
        print("1~3의 값을 입력하세요")