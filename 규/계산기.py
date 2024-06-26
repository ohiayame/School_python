def Calculator():
    while True:
        num1 = input("\n첫 번째 숫자를 입력하세요: ")
        try:
            num1 = int(num1)
            break
        except:
            print("유효한 숫자를 입력하세요")
            continue
    while True:
        num2 = input("두 번째 숫자를 입력하세요: ")
        try:
            num2 = int(num2)
            break
        except:
            print("유효한 숫자를 입력하세요")
            continue
    while True:
        operator = input("연산자를 입력하세요 (+, -, *, /): ")
            
        if operator == "+":
            ans = num1 + num2
            break
        elif operator == "-":
            ans = num1 - num2
            break
        elif operator == "*":
            ans = num1 * num2
            break
        elif operator == "/":
            ans = num1 / num2
            break
        else:
            print(("유효한 연산자를 입력하세요 (+, -, *, /): "))
        
    print(f"\n결과: {num1} {operator} {num2} = {ans}\n")

def ListSum():
    while True:
        input_num = input("\n정수 리스트를 입력하세요 (쉼표로 구분, 예: 1,2,3,4): ")
        try:
            input_li = list(map(int,input_num.split(",")))
            break
        except:
            continue
    sum = 0
    for n in input_li:
        sum += n
    print(f"\n리스트의 합: {sum}\n")

def Pibonaci():
    while True:
        input_len = input("\n피보나치 수열의 길이를 입력하세요: ")
        try:
            input_len = int(input_len)
            break
        except:
            continue
    p_li = [0]
    if input_len > 1:
        p_li.append(1)
        num1 = p_li[0]
        num2 = p_li[1]
    if input_len > 2:
        for _ in range(input_len-2):
            num = num1 + num2
            p_li.append(num)
            num1 = num2
            num2 = num
    print("피보나치 수열:",*p_li)

while True:
    print("메뉴:")
    print("1. 사칙연산 계산기")
    print("2. 리스트 합 계산")
    print("3. 피보나치 수열 출력")
    print("4. 종료")
    
    input_num = int(input("원하는 기능을 선택하세요: "))
    if input_num == 1:
        Calculator()
    elif input_num == 2:
        ListSum()
    elif input_num == 3:
        Pibonaci()
    elif input_num == 4:
        break
    else:
        print("제 입력해주세요")