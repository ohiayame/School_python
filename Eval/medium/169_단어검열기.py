# for문과 인덱스를 사용하여 금지어를 찾아 대체하세요.
sentence = input()
banned = input()

result = ""
skip = 0

# 문장을 반복
for i in range(len(sentence)):
    # 이미 바꾼 부분이면 건너뛰기
    if skip > 0:
        skip -= 1
        continue

    # 만약에 i번째 글자 ~ ban길이 만큼의 글이 ban와 동일하면 "***" 추가 하고 skip 정의
    if sentence[i : i + len(banned)] == banned:
        result += "***"
        skip = len(banned) - 1
    # 아니면 그대로 저장
    else:
        result += sentence[i]

print(result)