li_1 = []
li_2 = []
li_3 = []
li_4 = []
li_5 = []
for _ in range(5):
    char = str(input()) 
    for i in char:
        if _ == 0:
            li_1.append(i)
        if _ == 1:
            li_2.append(i)
        if _ == 2:
            li_3.append(i)
        if _ == 3:
            li_4.append(i)
        if _ == 4:
            li_5.append(i)
msg = ""
for i in range(15):
    if i < len(li_1):
        msg += str(li_1[i])
    if i < len(li_2):
        msg += str(li_2[i])
    if i < len(li_3):
        msg += str(li_3[i])
    if i < len(li_4):
        msg += str(li_4[i])
    if i < len(li_5):
        msg += str(li_5[i])
print(msg)

#############

# 다섯 개의 문자열을 저장할 리스트를 생성합니다.
words = []

# 다섯 줄에 걸쳐서 문자열을 입력받아 리스트에 저장합니다.
for i in range(5):
    word = input().strip()  # 문자열을 입력받고 양쪽 공백을 제거합니다.
    words.append(word)

# 세로로 읽은 문자열을 저장할 변수를 생성합니다.
result = ""

# 다섯 개의 문자열 중 가장 긴 문자열의 길이를 구합니다.
max_len = max(len(word) for word in words)

# 가장 긴 문자열의 길이만큼 반복합니다.
for i in range(max_len):

    # 다섯 개의 문자열을 세로로 읽어서 result에 추가합니다.
    for j in range(5):

        # i번째 위치에 문자가 있으면 추가합니다.
        if i < len(words[j]):
            result += words[j][i]

# 세로로 읽은 문자열을 출력합니다.
print(result)