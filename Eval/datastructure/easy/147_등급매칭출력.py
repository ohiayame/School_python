# items() 로 (이름, 점수) 동시 받아 등급 분기.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50, "Y": 60},
]
t = int(input())
scores = data_sets[t]

for name, score in scores.items():
    # A(90+), B(80~89), C(70~79), D(60~69), F(60 미만)
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # f-string f"{name}: {grade}" 출력
    print(f"{name}: {grade}")