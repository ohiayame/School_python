# For 문을 사용하여 아래 문자열 내 단어 개수를 출력
myString = "It is a great weather with you"
count = 1
for c in myString:
    if c == " ":
        count += 1
print("문자열 단어 갯수 : ", count)