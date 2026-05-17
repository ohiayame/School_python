# lower()로 소문자 변환 후 비교
text = input().lower() # 소문자 변환
vowel_count = 0

# 모음(a, e, i, o, u)
vowels = set('aeiou')

# 문자열 반복 vowels에 있으면 추가
for char in text:
    if char in vowels:
        vowel_count += 1

# 개수 출력
print("모음 개수:", vowel_count)