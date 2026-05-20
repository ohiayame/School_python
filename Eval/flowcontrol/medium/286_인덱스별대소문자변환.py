# 인덱스를 알아야 하므로 range로 순회하세요. 글자의 대소문자 변환은 문자열 메서드를 사용합니다.
text = input()

result = ""

for idx in range(len(text)):
    # 짝수 인덱스(0, 2, 4, ...)의 글자는 대문자로
    # 홀수 인덱스(1, 3, 5, ...)의 글자는 소문자로 변환
    if idx % 2 == 0:
        result += text[idx].upper()
    else:
        result += text[idx].lower()
        
# 결과 출력
print(result)