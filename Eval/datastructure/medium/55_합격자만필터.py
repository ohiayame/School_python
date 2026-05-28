# 원본 dict 의 items() 를 순회하면서 if 절로 합격 조건을 검사하세요.
students = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# dict 컴프리헨션으로 점수 >= cutoff 인 학생만의 dict 생성
cutoff_students = {name: score for name, score in students.items() if score >= cutoff}

# "이름: 점수" 형식으로 한 줄씩 출력
for name, score in cutoff_students.items():
    print(f"{name}: {score}")