# 누진세율: 구간별로 나누어 계산하세요
# 흐름: 연봉 입력 → 구간별 세금 누적 → 출력
salary = int(input())
tax = 0

# 1200만원 이하: 6%
if salary <= 1200:
    tax += salary * 0.06
else:
    tax += 1200 * 0.06

    # 1200만원 초과 ~ 4600만원 이하: 초과분 15%
    if salary <= 4600:
        tax += (salary - 1200) * 0.15
    else:
        tax += (4600 - 1200) * 0.15

        # 4600만원 초과: 초과분 24% (salary를 사용해야 하드코딩 버그 방지)
        tax += (salary - 4600) * 0.24

# 결과 값 출력
print(f"연봉: {salary}만원")
print(f"세금: {int(tax)}만원")