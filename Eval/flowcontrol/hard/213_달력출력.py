# 헤더 출력 후, 시작 요일에 맞춰 날짜를 배치하세요.
start_day = int(input())
last_date = int(input())

# 전체 행 수: 시작 오프셋(start_day-1) + 총 날짜를 7로 나눠 올림
rows = (start_day - 1 + last_date + 6) // 7  # 올림 나눗셈으로 필요한 행 수 계산
print("월  화  수  목  금  토  일")

current_start = 1  # 현재 행의 시작 날짜
for row in range(rows):
    if row == 0:
        # 첫 행: 시작 요일 앞 빈 슬롯(4칸씩) 출력
        print('    ' * (start_day - 1), end="")
        next_start = 9 - start_day  # 다음 행 시작 날짜 = 8 - (start_day-1)
    else:
        next_start = min(last_date, current_start + 6) + 1  # 행에 최대 7일

    # 날짜를 2자리 오른쪽 정렬 후 2칸 구분자로 연결
    print('  '.join(f"{day:2d}" for day in range(current_start, next_start)))
    current_start = next_start