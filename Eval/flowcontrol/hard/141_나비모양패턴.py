# 나비 모양 패턴을 출력하세요.
n = int(input())

total_width = 2 * n - 1  # 전체 너비: 2n-1
half = n // 2             # 가운데 기준 위/아래 줄 수

# 위쪽 절반: 별 1개부터 half개까지 증가
upper_lines = []
for star_count in range(1, half + 1):
    space_count = total_width - star_count * 2  # 가운데 공백 크기
    upper_lines.append("*" * star_count + " " * space_count + "*" * star_count)

# 위쪽 출력
for line in upper_lines:
    print(line)

# 가운데 줄
print("*" * total_width)

# 아래쪽 절반: 위쪽의 역순
for line in reversed(upper_lines):  # 중복 계산 없이 역순 재활용
    print(line)