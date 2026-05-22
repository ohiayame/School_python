# items() 로 (키, 값) 쌍을 받아 순회.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

for name, score in scores.items():
    print(f"{name}: {score}")