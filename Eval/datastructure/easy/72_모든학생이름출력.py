# dict 의 키들을 공백 구분으로 출력하세요.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

# dict 삽입 순서대로 공백 구분 한 줄에 출력
print(" ".join(scores))