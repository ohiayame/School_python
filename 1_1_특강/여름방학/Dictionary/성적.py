# 메뉴 함수
def MenuPrint():
    wight = 20
    
    print("=" * wight)
    print(" 1. 학생 성적 입력")
    print(" 2. 학생 목록 출력(입력 순)")
    print(" 3. 프로그램 종료")
    print("=" * wight)


# 입력 받기
def InputInf():
    lists = {}
    # 학번, 이름, 국어, 영어, 수학
    lists["id"] = input("학번을 입력하세요\n")
    lists["name"]  = input("이름을 입력하세요\n")
    lists["kor"] = int(input("국어 성적을 입력하세요\n"))
    lists["eng"] = int(input("영어 성적을 입력하세요\n"))
    lists["math"] = int(input("수학 성적을 입력하세요\n"))
    # 총점 계산
    lists["Sum"] = lists["kor"] + lists["eng"] + lists["math"]
    # 평균 계산
    lists["avg"] = round(lists["Sum"] / 3, 2)
    return lists

students = []
num = 0
# 3을 입력 받을 때 까지 반복
while True:
    MenuPrint()
    # 메뉴 입력 받기
    input_menu = int(input())
    
    # 정보 입력 받기
    if input_menu == 1:
        num += 1
        students.append(InputInf())

    
    # 목록을 출력 
    elif input_menu == 2:
        for i, student in enumerate(students, start=1):
            for key, value in student.items():
                print(f"{key}: {value}", end = " ")
            print()
    # 종료
    elif input_menu == 3:
        print("프로그램 종료")
        break
    
    # 예외 처리
    else:
        print("Error")