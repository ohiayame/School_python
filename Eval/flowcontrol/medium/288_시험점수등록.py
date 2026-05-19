# 등급별 카운터 4개를 0으로 초기화하고, 입력 0을 종료 조건으로 반복 처리하세요.
count_a = 0
count_b = 0
count_c = 0
count_f = 0

while True:
    score = int(input())
    if score == 0:
        break
    elif score < 0:
        print("잘못된 점수")
        continue
    # 점수가 100보다 크면: 점수 초과
    elif score > 100:
        print("점수 초과")
        continue
    
    # 90 이상 100 이하: A 카운트 +1
    if score >= 90:
        count_a += 1
    # 80 이상 89 이하: B 카운트 +1
    elif score >= 80:
        count_b += 1
    # 70 이상 79 이하: C 카운트 +1
    elif score >= 70:
        count_c += 1
    # 1ㅣ이상 69 이하: F 카운트 +1
    else:
        count_f += 1

print(f"A: {count_a} B: {count_b} C: {count_c} F: {count_f}")