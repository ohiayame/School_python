# for문으로 문자열을 순회하며 플래그를 사용하세요.
s = input()

isTrue_At = False    # @ 여부 확인 변수
isTrue_dot = False # . 여부 확인 변수

# 문자열 반복
for char in s:
    # @면 True로 재정의
    if char == "@":
        isTrue_At = True
    # .면 True로 재정의
    elif char == ".":
        isTrue_dot = True
    
    # @와 . 이 있으면 반복 강제 종료
    if isTrue_At and isTrue_dot:
        break

# @와 . 이 있으면 "유효" 출력
if isTrue_At and isTrue_dot:
    print("유효")
# 아니면 "무효" 출력
else:
    print("무효")