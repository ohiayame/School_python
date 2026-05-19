# 좌석번호를 열(A~J)과 번호(1~10)로 변환하세요
seat = int(input())

# 범위 밖(1 미만 또는 100 초과)이면: 잘못된 좌석번호입니다.
if seat < 1 or seat > 100:
    print("잘못된 좌석번호입니다.")
else:
    # 알파벳 계산: (seat-1)을 기준으로 열 인덱스 산출
    row_label = chr(ord("A") + (seat - 1) // 10)
    # 번호 계산: (seat-1) % 10 + 1 로 삼항식 없이 1~10 범위 보장
    seat_num = (seat - 1) % 10 + 1

    # 결과 값 출력
    print(f"좌석 {seat} → {row_label}열 {seat_num}번")