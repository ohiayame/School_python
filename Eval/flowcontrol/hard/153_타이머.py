# 분과 초 변수로 관리하고 while True로 감소시키세요.
minutes = int(input())
seconds = 0

while True:
    # M분 SS초 출력
    print(f"{minutes}분 {seconds:02d}초")

    if seconds == 0:
        # 0분 0초 출력 후 타이머 종료! 출력
        if minutes == 0:
            print("타이머 종료!")
            break
        # 1 감소시키고 초를 60로 설정
        else:
            minutes -= 1
            seconds = 60
    # 매 턴 초를 - 1
    seconds -= 1