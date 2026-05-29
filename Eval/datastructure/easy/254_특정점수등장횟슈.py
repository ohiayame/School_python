n = int(input())

# 점수와 찾을 점수 입력 받기
# int()로 변환해 타입을 통일합니다
scores = []
for s in input().split():
    scores.append(int(s))  # 문자열 → 정수 변환
target = int(input())  # 비교 대상도 정수로 받아야 타입이 일치합니다

# 리스트 안에서 target와 같은 원소 개수 조회 후 출력
match_count = scores.count(target)  # num → match_count: 역할을 명확히
print(f"{target}점: {match_count}명")