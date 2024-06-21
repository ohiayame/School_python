# 3, 6, 9 게임구현
for index in range(1, 60):
    value = str(index)  # 현 숫자(정수)를 문자열로 변환
    flag = False    # 현 숫자 내 3, 6, 9 숫자가 있는지 나타내는 플래그
    msg = ""
    
    # 문자열 개수 만큼 순회
    # 예) "34" -> 2번 순회, 첫 번째 "3", 두 번째"4"
    for index_char in value:
        # 현 문자가 3,6,9 중에 하나일 경우 "박수" 출력
        if index_char == "3" or index_char == "6" or index_char == "9":
            msg += "박수 "
            flag = True  # 현 숫자 내 3, 6, 9가 존재 함으로 플래그 ON
            
    if flag:    # 3, 6, 9 중에 하나
        print(msg)  # 박수 출력
    else:       # 3 6, 9 가 아닐 경우
        print(index)    # 숫자 출력