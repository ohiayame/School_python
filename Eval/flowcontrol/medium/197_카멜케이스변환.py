# for문으로 순회하며 '_' 다음 문자를 대문자로 변환하세요.
s = input()
result = ""
capitalize_next = False

# 문자열 반복
for char in s:
    # _로 capitalize_next가 True면 upper하고 추가
    if capitalize_next:
        result += char.upper()
        capitalize_next = False
    # _면 capitalize_next를 True로 변환
    elif char == "_":
        capitalize_next = True
    # 아니면 그대로 추가
    else:
        result += char

# 결과 값 출력
print(result)