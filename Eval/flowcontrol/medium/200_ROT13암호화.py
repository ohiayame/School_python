# for문으로 순회하며 ord(), chr()을 사용해 13칸 밀기를 구현하세요.
text = input()
result = ""

for char in text:
    # a~z의 알파벳을 13칸 뒤 글자로
    if 'a' <= char <= 'z':
        result += chr(ord('a') + (ord(char) - ord('a') + 13) % 26)
    # A~Z의 알파벳을 13칸 뒤 글자로
    elif 'A' <= char <= 'Z':
        result += chr(ord('A') + (ord(char) - ord('A') + 13) % 26)
    else:
        result += char
# 결과 값 출력
print(result)