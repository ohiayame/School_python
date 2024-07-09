# 메뉴 함수
def MenuPrint():
    print("\n[메뉴 선택]")
    print("1. 학생 성적 입력")
    print("2. 학생 성적 화면 출력")
    print("3. 학생 성적 파일 출력")
    print("4. 종료")

# 입력 받기
def InputInf():
    global lists
    # 이름, 국어, 영어, 수학
    name = input("학생 이름:")
    kor = int(input("국어 점수:"))
    eng = int(input("영어 점수:"))
    math = int(input("수학 점수:"))
    # 총점 계산
    Sum = kor + eng + math
    # 평균 계산
    avg = Sum / 3
    lists.append([name, kor, eng, math, Sum, round(avg, 2)])

# 석차
def level():
    num = 1
    value = list([li[4] for li in lists[1:]] for _  in range(2))
    for _ in range(len(value[0])):
        rank = max(value[0])
        value[1][value[0].index(rank)] = num
        value[0][value[0].index(rank)] = 0
        num += 1
        
    for i in range(len(value[0])):
        lists[i+1].append(value[1][i])

# 입력 값 리스트
lists = [["이름", "국어", "영어", "수학", "총접", "평균", "등수"]]

# 프로그렘 시작
while True:
    # 메뉴 출력
    MenuPrint()
    # 메뉴 입력 받기
    input_menu = int(input("메뉴를 선택하세요: "))
    
    # 정보 입력 받기
    if input_menu == 1:
        InputInf()
        for li in lists[1:]:
            if len(li) > 6:
                li.pop() 
        level()

    # 목록을 출력 
    elif input_menu == 2:
        print("[학생 성적 목록]")
        for li in lists:
            for i in li:
                print(i, end="\t")
            print()

    # 파일로 저장
    elif input_menu == 3:
        file_name = input("저장할 파일명을 입력하세요: ")
        # W로 폴더를 열어서 생성
        handler = open(f"1_1_특강/여름방학/다차원/{file_name}", 'w', encoding='utf-8')
        # 정보를 폴더에 옮기기
        for li in lists:
            for i in li:
                i = str(i)  # write는 문자열만 가능
                handler.write(i, end="\t")
            handler.write("\n")
        # CLOSE
        handler.close()
        print(f"성적 정보가 {file_name} 파일에 저장되었습니다.")
        
    # 종료
    elif input_menu == 4:
        print("프로그램 종료")
        break
    
    # 예외 처리
    else:
        print("Error")