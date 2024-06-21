input_msg = input("단어 입력:")

# 카운트 선언
count = 0

# 단어의 시작 위치 선언
word_start = 0

# 입력된 메시지의 길이
length = len(input_msg)

# 입력된 메시지를 반복
while word_start < length:
    # 공백이 아닌 문자의 위치 찾기
    while word_start < length and input_msg[word_start] == " ":
        word_start += 1
    
    # 단어의 끝 위치 찾기
    word_end = word_start
    while word_end < length and input_msg[word_end] != " ":
        word_end += 1
    
    # 추출된 단어
    word = input_msg[word_start:word_end]
    
    # 추출된 단어와 입력한 단어가 일치하는 경우 카운트 증가
    if word == input_msg:
        count += 1
    
    # 다음 단어의 시작 위치 설정
    word_start = word_end + 1

# 카운트 결과 출력
print("단어 {}의 출현 빈도:".format(input_msg), count)