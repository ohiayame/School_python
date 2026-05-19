# 뒤집은 문자열과 원본을 비교
text = input()
# reversed_text = ""

# # text를 뒤집은 문자열 만들기
# for idx in range(1, len(text)+1):
#     reversed_text += text[-idx]
reversed_text = text[::-1]

# 뒤집은 문자열과 원본을 비교하여 결과 출력
if text == reversed_text:
    print(f"{text}은(는) 회문입니다!")
else:
    print(f"{text}은(는) 회문이 아닙니다.")