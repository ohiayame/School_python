# 22시 이후 시간을 구분하여 야간수당을 계산하세요
wage = int(input())
hours = int(input())
start = int(input())

# 1. 기본급 계산
# 22시 이후 근무분은 시급의 1.5배를 적용
# max(0, ...)으로 start >= 22인 엣지케이스도 안전하게 처리
night_time = max(0, (start + hours) - 22)
day_time = hours - night_time

base_wage = day_time * wage + int(night_time * wage * 1.5)  # 소수점 버림

# 2. 주휴수당
# 기본 급여(야간 할증 포함)의 20%를 추가
allowance = base_wage * 20 // 100

# 총 급여
total = base_wage + allowance

# 결과 출력
print(f"시급: {wage}원 | 근무: {hours}시간 ({start}시 시작)")
print(f"기본급: {base_wage}원")
print(f"주휴수당: {allowance}원")
print(f"총 급여: {total}원")