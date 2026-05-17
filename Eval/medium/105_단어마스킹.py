# 인덱스 0과 len-1만 원래 글자, 나머지는 *
text = input()
result = ""

# len(text) 번 반복
for idx in range(len(text)):
    # 첫 글자와 마지막 글자만 그대로
    if idx == 0 or idx == len(text) - 1:
        result += text[idx]
    # 나머지는 *로 바꿔
    else:
        result += "*"

# 마스킹 결과: ... 형태로 출력
print("마스킹 결과:", result)