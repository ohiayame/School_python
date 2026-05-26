# 누적합으로 삼각수를 구하고, 전체 합도 함께 누적
n = int(input())
triangle_num = 0  # 현재 삼각수 값 (누적합) — accrue → 명사형으로 변경
total = 0         # 모든 삼각수의 합계

# k번째 삼각수를 순서대로 계산하고 출력
for k in range(1, n + 1):  # num → k: 문제의 T(K) 표기와 일치
    triangle_num += k
    total += triangle_num
    print(f"T({k}) = {triangle_num}")

# 합계 값 출력
print(f"합계: {total}")