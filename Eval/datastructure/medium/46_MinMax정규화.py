# min, max 를 먼저 구해두고 컴프리헨션 안에서 사용하세요. 각 값을 f-string의 `:.2f` 로 포맷.
data = [10, 20, 30, 40, 50, 60, 70, 80]
n = int(input())  # 입력은 항상 2 이상 8 이하

# 슬라이스를 변수로 분리해 중복 참조 제거
subset = data[:n]

# min, max 를 먼저 구하기
max_num = max(subset)
min_num = min(subset)

# 리스트 컴프리헨션으로 min-max 정규화 후 바로 출력
print(" ".join(f"{(num - min_num) / (max_num - min_num):.2f}" for num in subset))