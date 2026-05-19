# N번 반복하며 점수를 입력받습니다. 범위를 벗어나면 안내 출력 후 continue, 유효한 점수만 누적합에 더하세요.
# 반복문 종료 후 최종 합계를 한 줄 출력합니다.
n = int(input())
total = 0

for _ in range(n):
    score = int(input())  # input_val → score: 도메인(점수)을 명확히 표현
    # 0 미만 또는 100 초과 시 "무효: X" 형식으로 출력하고 continue로 건너뜁니다.
    if not (0 <= score <= 100):  # 연쇄 비교로 범위 체크를 직관적으로 표현
        print(f"무효: {score}")
        continue
    # 유효한 점수는 total에 누적
    total += score

# 결과 출력
print(f"유효 점수의 합: {total}")