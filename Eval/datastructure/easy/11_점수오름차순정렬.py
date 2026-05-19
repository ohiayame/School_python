# 정수 리스트를 오름차순 정렬해 공백 구분 한 줄로 출력하세요.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [3, 1, 2],
    [50],
]
t = int(input())
scores = data_sets[t]

# map로 각 원소를 str로 변환하여 sorted로 정렬 후 출력
print(" ".join(map(str, sorted(scores))))