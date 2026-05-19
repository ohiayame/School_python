# for문으로 한 글자씩 생성하세요.
n = int(input())

# 비밀번호 저장 변수
password = ""

# n번 반복
for i in range(n):
    # 짝수는 알파벳
    if i % 2 == 0:
        # ord('a')로 알파벳 번호 가져오기
        # i는 항상 짝수 -> i // 2로 알파벳이 1씩 증가하게
        # 알파벳은 26개임으로 26로 나눔
        # -> 해당 알파벳을 문자로 변환하여 password에 추가
        password += chr(ord('a') + (i // 2) % 26)
    # 홀수는 숫자
    else:
        # (i // 2) + 1 로 순서대로 숫자 계산
        # 숫자는 0~9의 10개 -> 10으로 나눠 나머지를 password에 추가
        password += str(((i // 2) + 1) % 10)

# 만든 password를 출력
print(password)