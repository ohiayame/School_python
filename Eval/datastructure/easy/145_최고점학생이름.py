# strict greater 비교로 첫 본 학생 유지.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

# 가장 높은 점수를 받은 학생의 이름과 점수 저장
top_name = ""
top_score = float('-inf')

# items() 순회하며 비교
for name, score in scores.items():
    if score > top_score:
        top_name = name
        top_score = score

# 결과 값 출력
print(top_name)