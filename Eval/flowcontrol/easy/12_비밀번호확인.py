"""
TITLE: 비밀번호 확인
DIFFICULTY: easy
TAGS: if, else, string, comparison

EVAL: stdio

DESCRIPTION:
미리 설정된 비밀번호는 `python123`입니다. 입력된 비밀번호가 맞으면 `로그인 성공`을 출력하고,
틀리면 두 줄에 걸쳐 `비밀번호 오류`와 `다시 시도하세요`를 출력하시오.

예시:
- 입력: `python123` → 출력: `로그인 성공`
- 입력: `hello` → 출력: `비밀번호 오류\n다시 시도하세요`
"""

# 설정된 비밀번호와 입력값을 비교하세요.
password = "python123"
user_input = input()

# 입력값이 password와 동일하면 "로그인 성공" 출력
if user_input == password:
    print("로그인 성공")
# 아니면 "비밀번호 오류", "다시 시도하세요" 출력
else:
    print("비밀번호 오류")
    print("다시 시도하세요")