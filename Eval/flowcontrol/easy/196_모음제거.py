# for문으로 순회하며 모음 여부를 확인하세요.
s = input()
result = ""

# 비교를 위해 영어 모음 생성
vowel = 'aeiouAEIOU'

# 문자열을 순회
for char in s:
    # 만약에 글자가 vowel에 없으면 result에 추가
    if char not in vowel:
        result += char

# 결과 값 출력
print(result) 