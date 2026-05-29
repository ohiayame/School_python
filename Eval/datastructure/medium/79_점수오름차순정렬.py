# 점수가 동률인 경우 이름 알파벳순으로 자동 정렬됨.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"A": 50, "B": 50, "C": 50},
]
t = int(input())
scores = data_sets[t]

# (점수, 이름) tuple 리스트로 변환한 뒤 sort()
sort_scores = [(s, n) for n, s in scores.items()]
sort_scores.sort()

# 정렬된 list 를 다시 for s, n in pairs: 형태로 순회 이름: 점수 형식으로 한 줄씩 출력
for score, name in sort_scores:
    print(f"{name}: {score}")