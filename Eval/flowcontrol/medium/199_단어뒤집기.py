# for문으로 순회하며 단어를 모으고 공백을 만나면 뒤집으세요.
s = input()
result = ""
word = ""

# 문자 열 반복
for char in s:
    # 공백이면 word+" "를 result에 추가하고 word초기화
    if char == " ":
        result += word + " "
        word = ""
    # word에 char 추가
    else:
        word = char + word
# 마지막에 남아있는 word를 추가
result += word

# 결과 값 출력
print(result)