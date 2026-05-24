# zip 으로 두 list 원소를 동시에 받아 순회.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["X", "Y"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 두 시퀀스를 짝지어 (a_i, b_i) tuple 반환
for name, score in zip(names, scores):
    # f-string f"{name}: {score}" 으로 깔끔하게 포맷
    print(f"{name}: {score}")