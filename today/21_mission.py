# 문자열 검색을 위한 사전 임력 문장
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 단어의 개수
msg_li = sentence.split()
msg_li = [i for i in msg_li]

# 문자의 수
cher_li = sentence.replace(" ","")
cher_li = [j for j in cher_li]
    
# 문자열의 위치
def num_msg(msg):
    li = [] # 위치
    m = ""  # 단어
    n = 0   # 줄
    for i in range(len(sentence)):
        m += sentence[i]
        # 위치: i는 현제 위치, 해당단어의 길이(공백은 빼고)를 빼고 개행 1번당 더하기 4
        if (sentence[i] == " " and (m.replace(" ","")) == msg) or (sentence[i] == "\n" and (m.replace("\n","")) == msg) :
            l = (i - (len(m)-1) + (4 * n))
            li.append(l)
        # 공백이나 개행이 있을 경우에는 초기화, 개행 수를 세우기
        if sentence[i] == "\n" or sentence[i] == " ":
            if sentence[i] == "\n":
                n += 1
            m = ""
    # 마지막꺼 확인
    if m == msg:
        l = i - (len(m)-1)+ (4 * n)
        li.append(l)
    return li, n


# 문자열을 입력 받고 해당 문자열이 있는지, 몇개 있는지를 확인 
while True:
    input_msg = input("검색할 문자열을 입력하세요: ")
    # 입력 값이 문자열에 있는지 확인
    c = 0
    for m in msg_li:
        if m == input_msg:
            c += 1
    if c > 0:
        print("검색된 문자열의 개수:",c)
        break
    print("해당 문자열이 없습니다. 다시 입력해주세요.")

# 문자열의 위치과 줄 수 함수 호출
li, n = num_msg(input_msg)
print("검색된 문자열의 위치:",li)

# 단어의 개수와 전체문자의 수를 출력 
print(f"단어의 개수: {len(msg_li)}\n전체 문자 수: {len(cher_li)-n}")
print("줄 수:", n + 1)