# 무한 루프 안에서 0 입력 시 BYE 출력 후 break, 그 외는 범위별 분기 후 카운트.
total = 0

while True:
    num = int(input())

    if num == 0:
        print("BYE")
        break
    # 1~10번 → 비즈니스석 예약 출력, 예약 카운트 +1
    elif 1 <= num <= 10:
        print("비즈니스석 예약")
        total += 1
    # 11~20번 → 일반석 예약 출력, 예약 카운트 +1
    elif 11 <= num <= 20:
        print("일반석 예약")
        total += 1
    # 21~30번 → 이코노미석 예약 출력, 예약 카운트 +1
    elif 21 <= num <= 30:
        print("이코노미석 예약")
        total += 1
    # 그 외 (음수, 31 이상) → 잘못된 좌석 출력 (카운트 안 함, 다음 입력으로 진행)
    else:
        print("잘못된 좌석")

print(f"총 예약: {total}건")