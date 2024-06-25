# LAB 8
# 입력받은 문자가 모음（母音）인지 아닌지 확인
# 사용자로부터 하나의 영문자를 입력받는다
input_word = input("한 문자를 입력하세요: ")

# 입력받은 문자가 모음인지 아닌지 확인
if input_word == 'a' or input_word == "e" or input_word == "i" or input_word == "o" or input_word == "u" :
    print(input_word, "는 모음입니다.")       
else:
    print(input_word, "는 모음이 아닙니다.")