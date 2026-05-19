# 등급별 카운터 5개를 두고 N번 반복하며 입력 점수에 맞는 카운터를 증가시키세요.
n = int(input())

# 등급 정보: (등급명, 최솟값, 최댓값) — 정수로 통일해 타입 일관성 유지
score_levels = [
    ("A", 90, 100),
    ("B", 80,  89),
    ("C", 70,  79),
    ("D", 60,  69),
    ("F",  0,  59),
]

# 등급별 카운터 초기화
score_map = {rank: 0 for rank, _, _ in score_levels}

for _ in range(n):
    # 입력 값은 항상 0 ~ 100 사이
    score = int(input())

    # A: 90 이상 100 이하
    if score >= 90:
        score_map["A"] += 1
    # B: 80 이상 89 이하
    elif score >= 80:
        score_map["B"] += 1
    # C: 70 이상 79 이하
    elif score >= 70:
        score_map["C"] += 1
    # D: 60 이상 69 이하
    elif score >= 60:
        score_map["D"] += 1
    else:
        score_map["F"] += 1

# 결과 값 출력 (F 행은 최솟값 앞에 공백 1칸을 포맷으로 처리)
for rank, min_score, max_score in score_levels:
    print(f"{rank} ({min_score:2}~{max_score}): {score_map[rank]}명")