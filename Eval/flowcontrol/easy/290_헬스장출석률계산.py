# 출석일 수를 카운트한 뒤 백분율을 계산하고, 소수점 첫째 자리까지 포맷팅 출력하세요.
record = input()

# O 개수를 내장 메서드로 한 번에 카운트
attend_count = record.count('O')

# 출석률 계산 (출석 수 / 전체 일수 * 100)
attendance_rate = attend_count / len(record) * 100

print(f"출석률: {attendance_rate:.1f}%")