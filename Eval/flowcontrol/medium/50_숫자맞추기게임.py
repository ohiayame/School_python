# while True 안에서 정답일 때 break 하세요.
answer = 42

# 정답을 맞출 때까지 반복
while True:
    # 입력 받기
    value = int(input())
    # 정답을 맞추면 정답입니다!를 출력하고 종료
    if value == answer:
        print("정답입니다!")
        break
    # 입력한 수가 정답보다 작으면 "더 큰 수를 입력하세요" 출력
    elif value < answer:
        print("더 큰 수를 입력하세요")
    # 아니면(크면) "더 작은 수를 입력하세요" 출력
    else:
        print("더 작은 수를 입력하세요")