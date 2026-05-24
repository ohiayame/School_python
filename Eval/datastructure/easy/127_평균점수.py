# 합 / 개수로 평균 산출, `:.1f` 포맷.
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]
# 평균 계산
avg = sum(scores) / len(scores)
# 평균: X.X 형식으로 출력 (f-string {값:.1f}: 소수점 첫째 자리)
print(f"평균: {avg:.1f}")