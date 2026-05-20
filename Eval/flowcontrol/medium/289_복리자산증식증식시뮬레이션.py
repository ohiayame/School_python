# 정수 나눗셈(//)을 사용해야 예시 값과 정확히 일치합니다. 연도를 세는 변수 + 두 종료 조건의 순서를 결정하세요.
principal = int(input())      # 원금(만원)
annual_rate = int(input())    # 연이율(%)
target_amount = int(input())  # 목표 금액(만원)

# 자산을 원금으로 초기화
current_asset = principal

# for-else 구조: break 없이 루프를 완료하면 else 블록 실행
for year in range(1, 51):
    # 자산 = 자산 + (자산 * 이율) // 100
    current_asset = current_asset + (current_asset * annual_rate) // 100

    # 조건 1: 목표 도달 시 즉시 종료
    if current_asset >= target_amount:
        print(f"{year}년 차에 목표 도달 (자산: {current_asset}만원)")
        break
else:
    # 조건 2: 50년 내 미도달 — for 루프가 break 없이 종료된 경우
    print("50년 안에 도달 불가")