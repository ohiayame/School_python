# for문과 isupper(), islower(), isdigit()를 사용하세요.
s = input()
upper = 0
lower = 0
digit = 0
other = 0

# 각각 조건에 맞는 변수에 +1 
for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    else:
        other += 1

# 결과 값 출력
print(f"대문자: {upper}")
print(f"소문자: {lower}")
print(f"숫자: {digit}")
print(f"기타: {other}")