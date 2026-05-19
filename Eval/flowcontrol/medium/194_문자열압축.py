# for문으로 순회하며 이전 문자와 현재 문자를 비교하세요.
s = input()
result = ""

count = 1
# len(s) 반복
for idx in range(len(s)):
    # 나머지 한개이상 남아있고 지금 값과 다음값이 동일하면
    if idx + 1 < len(s) and s[idx] == s[idx + 1] :
        # +1
        count += 1
    # 아니면 result에 추가하고 초기화
    else:
        result += s[idx]
        result += str(count)
        count = 1
        
# 결과 값 출력
print(result)