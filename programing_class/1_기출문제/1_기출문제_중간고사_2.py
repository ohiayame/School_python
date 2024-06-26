# 출력
# --------------------------
# 1. 홀수 짝수 구분 프로그램
# 2. 3의 배수 확인 프로그램
# --------------------------
print("--------------------------")
print("1. 홀수 짝수 구분 프로그램")
print("2. 3의 배수 확인 프로그램")
print("--------------------------")
# 함수
def program(menu,value):
    if menu == 1: 
        # if 정수가 2나머지 0 면 -> 짝수
        if value % 2 == 0:
            msg =  "짝수입니다."
        # 아니면 -> 홀수
        else:
            msg =  "홀수입니다."
            
    elif menu == 2:
        # if 정수가 3나머지 0 면 -> 3의 배수
        if value % 3 == 0:
            msg = "3의 배수입니다"
        # 아니면 -> 3의 배수 아니다 
        else:
            msg = "3의 배수가 아닙니다."   
    return msg

# 출력(메뉴를 선택해 주십시오.
print("메뉴를 선택해 주십시오.")
# 메뉴를 입력 받기
menu = int(input())
if menu == 1 or menu == 2:
    if menu == 1: 
        # 출력 (홀수 짝수 구분 프로그램을 선택 하셨습니다.
        print("홀수 짝수 구분 프로그램을 선택 하셨습니다.")
    else:
        # 출력(3의 배수 확인 프로그램을 선택 하셨습니다.
        print("3의 배수 확인 프로그램을 선택 하셨습니다.")  

    # 출력 (정수 값을 입력 하세요.
    print("정수 값을 입력 하세요.")
    # 사용자로부터 정수를 입력 받는다
    value = int(input())
        
    # 출력 (입력하신 값 (정수), 함수(결과 msg) )   
    print("입력하신 값", value, ",", program(menu,value))
# else
else:
    # 출력 (입력하신 값 ()은 유효하지 않은 메뉴 선택 값입니다. 메뉴 선택은 1과 2만 가능합니다.
    print(f"입력하신 값 {menu}은 유효하지 않은 메뉴 선택 값입니다. 메뉴 선택은 1과 2만 가능합니다.")