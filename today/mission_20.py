# 문자열 입력받기 split
msg = input("문자열 입력:") #.split()       
        
# 사용자 지정 단어 입력받기
input_msg = input("단어 입력:")

word = ""
# 카운트 선언
count = 0

for char in msg :
    if char != " ":
        word += char
    else:
        if input_msg == word:
            count += 1
        word = ""    
            
if input_msg == word:
            count += 1
        
# 카운트 결과를 출력
print("단어{}의 출현 빈도:".format(input_msg), count)