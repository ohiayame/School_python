# 문자열도 시퀀스이므로 `for c in s` 로 한 글자씩 순회할 수 있습니다. 숫자/기호는 upper() 영향을 받지 않습니다.
s = input()

# 각 글자를 대문자로 변환한 리스트를 공백으로 구분하여 한 줄에 출력
char_arr = [char.upper() for char in s]
print(" ".join(char_arr))