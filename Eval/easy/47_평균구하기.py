"""
[문제]
    숫자를 반복해서 입력받고,
    0이 입력되면 종료합니다.
    입력한 숫자(0 제외)들의 평균을 (평균: 값) 형식(f-string, float 결과)으로 출력하시오.
    단, 입력한 숫자가 하나도 없으면 입력한 숫자가 없습니다.를 출력하시오.
    첫 입력을 먼저 받고, while num != 0 으로 반복하며 다음 입력을 받으세요.
"""
total = 0
count = 0

# 첫 입력을 먼저 받기
num = int(input())

# 첫 입력이 0이면 "입력한 숫자가 없습니다." 출력
if num == 0:
    print("입력한 숫자가 없습니다.")
else:
    # 0이 입력될 때까지 반복
    while num != 0:
        # total에 입력된 값을 추가
        total += num
        # count에 1 더하기
        count += 1
        # 다음 입력 받기
        num = int(input())

    # 평균 계산 및 출력
    average = total / count
    # 평균: 값 형식으로 평균을 출력(소수점 1자리)
    print(f"평균: {average:.1f}")