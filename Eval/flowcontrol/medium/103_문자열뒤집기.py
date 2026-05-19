# range(len(text)-1, -1, -1)로 역순 순회
text = input()
result = ""

#  for + range로 거꾸로 뒤집어 result에 저장
for idx in range(len(text)-1, -1, -1):
    result += text[idx]

# 뒤집은 문자열: ... 형태로 출력
print("뒤집은 문자열:", result)