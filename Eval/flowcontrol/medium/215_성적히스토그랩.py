# 구간별 개수를 세고, 0이 아닌 구간만 출력하세요.
n = int(input())

# 리스트 인덱스 0~9가 각 10점 구간에 대응 (인덱스 9 = 90~100)
counts = [0] * 10

for _ in range(n):
    # 항상 (0~100 정수)가 입력
    score = int(input())
    # 100이면 level = 9
    if score == 100:
        level = 9
    else:
        # 아니면 10의 자리
        level = score // 10
    counts[level] += 1  # 딕셔너리 대신 리스트로 카운트 — 문자열 정렬 위험 없음

# 출력
for level, count in enumerate(counts):
    if count == 0:  # 인원이 없는 구간은 출력하지 않음
        continue
    if level == 9:
        print(f"90~100: {'#' * count}")
    else:
        print(f"{level}0~{level}9: {'#' * count}")