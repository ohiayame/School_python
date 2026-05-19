# for문과 플래그 변수를 사용하세요. upper() 메서드를 활용하세요.
s = input()
result = []
capitalize_next = True  # isTrue → 역할이 명확한 이름으로 변경

# 문자열 반복
for char in s:
    if capitalize_next:
        result.append(char.upper())  # 리스트에 추가 후 join으로 합치면 성능 향상
        capitalize_next = False
    else:
        result.append(char)

    # 공백이면 다음 글자를 대문자로 처리
    if char == " ":
        capitalize_next = True

# 결과 값 출력
print("".join(result))  # 문자열 연결 대신 join 사용