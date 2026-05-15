# for문으로 순회하며 '('와 ')'의 개수를 각각 세세요.
s = input()

bracket_start = 0  # '(' 개수
bracket_end = 0    # ')' 개수

# 문자열 반복
for char in s:
    # '(' 면 bracket_start 더하기 1
    if char == "(":
        bracket_start += 1
    # ')' 면 bracket_end 더하기 1
    elif char == ")":
        bracket_end += 1

# '('와 ')'의 개수가 같으면 "올바름" 출력
if bracket_start == bracket_end:
    print("올바름")
# 아니면 "올바르지 않음" 출력
else:
    print("올바르지 않음")