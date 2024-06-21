# 문자열 입력받기 split
msg = input("문자열 입력:") #.split()       
        
# 사용자 지정 단어 입력받기
input_msg = input("단어 입력:")

# word 선언
word = ""
# 카운트 선언
count = 0

# msg를 반복
for char in msg :
    # 공백 아니면 word에 추가
    if char != " ":
        word += char
    # 아니면 
    else:
        # word == 지정 단어면 count +1
        if input_msg == word:
            count += 1
        # word 초기화 
        word = ""   

# 마지막 word 검사 -> word == 지정 단어면 count +1           
if input_msg == word:
            count += 1
        
# 카운트 결과를 출력
print("단어{}의 출현 빈도:".format(input_msg), count)