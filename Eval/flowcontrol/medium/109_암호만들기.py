# ord/chr와 z/Z 순환 처리
text = input()
result = ""

for char in text:
    # a~z의 알파벳을 다음 글자로
    if 'a' <= char <= 'z':
        result += chr(ord('a') + (ord(char) - ord('a') + 1) % 26)
    # A~Z의 알파벳을 다음 글자로
    elif 'A' <= char <= 'Z':
        result += chr(ord('A') + (ord(char) - ord('A') + 1) % 26)
    # 이외 그대로
    else:
        result += char

# 결과 값 출력
print("암호:", result)