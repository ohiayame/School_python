# For 문을 사용하여 아래 문자열 내 ‘h’의 개수를 출력

myString = "hello hyundai hoho"
count = 0
for char in myString:
    if char == "h":
        count += 1
print("문자열 내 h 갯수 :", count)