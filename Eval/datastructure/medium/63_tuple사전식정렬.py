# (점수, 이름) tuple 의 자연스러운 정렬을 활용하세요.
data_sets = [
    [(85, "윤서"), (92, "지우"), (65, "민준"), (78, "서윤"), (95, "도윤")],
    [(80, "A"), (70, "B"), (90, "C")],
    [(50, "혼자")],
]
t = int(input())
students = sorted(data_sets[t]) # 정렬

# 이름: 점수 형식으로 한 줄씩 출력
for score, name in students:
    print(f"{name}: {score}")