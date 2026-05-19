# `reverse=True` 인자가 핵심입니다.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]
t = int(input())
scores = data_sets[t]

# 내림차순 정렬 후 공백으로 구분하여 한 줄 출력
print(" ".join(map(str, sorted(scores, reverse=True))))