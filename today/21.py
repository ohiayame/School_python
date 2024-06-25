# 문자열 검색을 위한 사전 입력 문장
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

def chercheck(input_msg, String):

    index = 0     # 입력 받은 글짜의 인덱스 값
    all_ = 0      # 모든 글자 (공백 개행 포함)
    index_li = [] # 입력 받은 단어가 문자열의 어디에 있는지 -> 입력 받은 단어의 제일 앞 글자의 인덱스 값을 저장
    msg_count = 0 # 단어의 개수
    b_cher = ""   # 이전 글자
    all_msg = 0   # 단어의 개수
    enter = 1     # 줄 수
    all_cher = 0  # 전체 문자 수

    for cher in String:
        # 모든 글자를 세우기
        all_ += 1
        
        # 1) 입력 받은 문자와 같은 글자가 있는지 확인
        # 만약에 입력받은 문자의 글자와 문자열의 글자가 연속적으로(입력받은 문자의 길이 만큼) 같은 경우
        if input_msg[index] == cher:
            index += 1
            if index == len(input_msg):
                # 모든 글자(입력받은 문자 포함) 빼기 입력받은 문자의 길이
                index_li.append(all_ - len(input_msg))
                # 인덱스 초기화
                index = 0
                # 2) 단어의 개수
                msg_count += 1
        # 인덱스 초기화
        else:  
            index = 0
        
        # 3) 공백 또는 개행문자 때 -> 이전 글짜가 공백, 개행문자 아니면 단어를 추가
        if cher == ' ' or cher == "\n":
            if b_cher!= " " and b_cher != "\n":
                all_msg += 1
            # 4) 개행 문자로 줄 세우기
            if cher == "\n":  
                enter += 1
                
        # 5) 문자열의 마지막 글자 처리(문자열의 길이와 모든 글자의 수가 같을 때)
        elif all_ == len(String):
            # 이전 글자와 현재 글짜가 공백 또는 개행문자 아닐 때 단어를 추가 (37번 라인이 해당되지 않을 때만 45번 라인이 실행 됨)
            if b_cher != " " and b_cher != "\n":
                all_msg += 1
                
        # 6) 공백 또는 개행문자 아닐 때 -> 글자 수 세우기 (37번, 45번 라인이 해당되지 않을 때만 50번 라인이 실행 됨)
        else:
            all_cher += 1
            
        # 현재 글자를 지정해서 다음에 반복할 때 이전 글자를 확인할 수 있게 한다
        b_cher = cher
    
    # 반복이 종료 후  
    # 7) 만약에 문자열의 개수가 0일 때 True를 반환 -> 함수 종료
    if msg_count == 0:
        return True
    
    # 8) 결과 출력
    print("검색된 문자열의 개수:", msg_count)
    print("검색된 문자열의 위치:", index_li)
    print("단어의 개수:", all_msg)
    print("전체 문자 수:", all_cher)
    print("줄 수:", enter)

while True:
    # 글자를 입력 받기
    input_msg = input("검색할 문자열을 입력하세요: ")
    
    # 문자열의 개수가 0일 때 True가 돌아 온다 
    # 만약에 True일 경우 반복
    if chercheck(input_msg, sentence):
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
    # 아니면 반복 종료 -> 이걸 안하면 결과를 출력해도 무한 반복이 됨
    else:
        break