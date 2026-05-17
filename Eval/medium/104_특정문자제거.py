# for + if char != remove: result += char
text = input()
remove = input()
result = ""

# text 한 글자 씩 반복
for char in text:
    # char != remove면 result에 추가
    if char != remove:
        result += char

# 출력
print("결과:", result)