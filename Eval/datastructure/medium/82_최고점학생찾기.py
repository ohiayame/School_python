# strict greater (>) 비교로 첫 본 학생을 유지.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

top_name, top_score = "", float('-inf')

# for name, score in d.items(): 로 순회하며 strict greater 비교하고 갱신
for name, score in scores.items():
    if top_score < score:
        top_name, top_score = name, score

print(f"{top_name}: {top_score}")