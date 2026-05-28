# zip 으로 두 리스트의 원소를 동시에 받아 컴프리헨션 안에서 사용.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B"],
    ["solo"],
]
scores_sets = [
    [85, 92, 78, 95, 88],
    [100, 200],
    [42],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 컴프리헨션: [f"{n}={s}" for n, s in zip(names, scores)]으로 두 시퀀스를 짝지어 출력
print(*[f"{n}={s}" for n, s in zip(names, scores)])