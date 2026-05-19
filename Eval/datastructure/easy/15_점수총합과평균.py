# 합과 개수로 평균을 구하고 소수점 첫째 자리 포맷으로 출력하세요.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 70],
    [100],
]
t = int(input())
scores = data_sets[t]

# 총합과 평균 계산
total = sum(scores)
average = total / len(scores)

# 결과 값 출력
print(f"총합: {total}")
print(f"평균: {average:.1f}")