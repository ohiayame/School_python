# while True로 반복, if/elif로 경우 분기
current = 1

# 층 번호를 표시 문자열로 변환하는 헬퍼 함수 (중복 제거)
def floor_name(n):
    """층 번호를 표시 문자열로 변환 (-1 → 'B1층', 그 외 → 'N층')"""
    return 'B1층' if n == -1 else f'{n}층'

while True:
    # 1. 현재 층: X층 (지하면 B1층) 출력
    print(f"현재 층: {floor_name(current)}")

    # 2. 이동할 층 입력
    target_floor = int(input())

    # 3. 입력이 0이면 엘리베이터를 종료합니다. 출력 후 종료
    if target_floor == 0:
        print("엘리베이터를 종료합니다.")
        break

    # 범위(-1~10) 밖이면 오류 메시지 출력 후 빈 줄 하나 출력하고 다음 반복
    elif target_floor < -1 or target_floor > 10:
        print("이동할 수 없는 층입니다. (-1 ~ 10)")
        print()

    # 현재 층과 같으면 이미 해당 층에 있습니다. 출력 후 빈 줄 하나 출력하고 다음 반복
    elif target_floor == current:
        print("이미 해당 층에 있습니다.")
        print()

    # 이동 과정: 시작층 → ... → 목표층 한 줄에 출력 (0층은 건너뜀)
    else:
        # 이동 방향 결정 (+1 올라감, -1 내려감)
        step = 1 if target_floor > current else -1
        # target_floor 포함을 위해 +step, 0층은 건너뜀
        move_path = [
            floor_name(num)
            for num in range(current, target_floor + step, step)
            if num != 0
        ]

        # 현재 층 갱신 (내부 상태는 -1 그대로 유지, 0으로 바꾸지 않음)
        current = target_floor

        # 결과 값 출력
        print(" → ".join(move_path))
        print(f"{floor_name(current)}에 도착했습니다.")
        print()  # 이동 성공 후 빈 줄