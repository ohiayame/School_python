# 점수를 tuple 의 첫 자리로 두면 sort 만으로 점수 기준 정렬.
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

# (점수, 이름) tuple 리스트 만들기: [(s, n) for n, s in zip(names, scores)] / sorted() 로 정렬
score_names = sorted([(score, name) for name, score in zip(names, scores)])

# 결과를 이름: 점수 형식으로 한 줄씩 출력
for score, name in score_names:
    print(f"{name}: {score}")