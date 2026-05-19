# print(char.upper(), end="")로 이어 출력
text = input()

# 한 글자씩 대문자로 변환하여 한 줄에 이어서 출력
for char in text:
    print(char.upper(), end="")
# 마지막에 줄바꿈
print()