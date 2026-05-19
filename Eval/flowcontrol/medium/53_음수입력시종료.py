# while True 안에서 음수면 break, 아니면 total에 누적.
# 출력은 print("합계:", total) — 콤마로 공백 하나 포함
total = 0

# 음수가 입력될 때까지 반복
while True:
    # 입력 받기
    num = int(input())
    # 음수이면 강제 종료
    if num < 0:
        break
    # 아니면(양수이면) total에 추가
    total += num

# total 출력
print("합계:", total)