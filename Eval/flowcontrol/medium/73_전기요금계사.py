# 구간별로 나눠 계산하세요.
usage = int(input())

# 문제에 적혀있는 조건으로 요금 구하기
if usage <= 100: 
    charge = usage * 60
elif 100 < usage <= 200:
    charge = 100 * 60 + (usage - 100) * 120
else:
    charge = 100 * 60 + 100 * 120 + (usage - 200) * 190

# 부가세 계산
tax = int(charge * 0.1)

# 결과 값 출력
print(f"전기 요금: {charge}원")
print(f"부가세 (10%): {tax}원")
print(f"총 납부 금액: {charge + tax}원")