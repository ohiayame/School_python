# 이중 반복문과 배치 카운트로 구현하세요.
n = int(input())
m = int(input())

# 총 행 수를 미리 계산 (나머지가 있으면 +1)
total_rows = (n + m - 1) // m

for row in range(1, total_rows + 1):
    row_seats = []  # 현재 행의 좌석 번호 임시 저장 배열

    # 이 행에 배치할 열 수: 마지막 행은 남은 인원만큼만
    cols_in_row = min(m, n - (row - 1) * m)

    for col in range(1, cols_in_row + 1):
        row_seats.append(f"{row}-{col}")

    # 각 행 출력
    print(f"[{row}행]", "  ".join(row_seats))

print(f"총 {total_rows}행 배치 완료 ({n}명)")