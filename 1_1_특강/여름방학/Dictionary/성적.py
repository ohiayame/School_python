# 메뉴 함수
def MenuPrint(value, avg):
    wight = 20
    
    print("=" * wight)
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력(입력 순)")
    print(" 3. 프로그램 종료")
    
    # 입력데이터의 개수 출력
    print(f"\n현 입력데이터 갯수: {value}")
    # 전체 학생 평균을 출력
    print(f"전체 학생 평균 값  : {avg:.2f}")
    print("=" * wight)

# 입력 받기
def InputInf():
    global lists
    # 학번, 이름, 국어, 영어, 수학
    num = input("학번을 입력하세요\n")
    name = input("이름을 입력하세요\n")
    kor = int(input("국어 성적을 입력하세요\n"))
    eng = int(input("영어 성적을 입력하세요\n"))
    math = int(input("수학 성적을 입력하세요\n"))
    # 총점 계산
    Sum = kor + eng + math
    # 평균 계산
    avg = Sum / 3
    lists.append([num, name, kor, eng, math, Sum, round(avg, 2)])

# 입력 값 리스트
lists = []
# 키 리스트
keys = ["id", "name", "kor", "eng" "math", "sum", " avg"]
avg = 0.0
Sum = 0
# 3을 입력 받을 때 까지 반복
while True:
    MenuPrint(len(lists), avg) # 데이터 갯수, 평균
    # 메뉴 입력 받기
    input_menu = int(input())
    
    # 정보 입력 받기
    if input_menu == 1:
        InputInf()
        # 입력 받은 avg를 더하여 평균을 계산
        Sum += lists[-1][6]
        avg = Sum / len(lists)
    
    # 목록을 출력 
    elif input_menu == 2:
        for i in range(len(lists)):
            my_dict = dict(zip(keys, lists[i]))
            print(my_dict)
    
    # 종료
    elif input_menu == 3:
        print("프로그램 종료")
        break
    
    # 예외 처리
    else:
        print("Error")