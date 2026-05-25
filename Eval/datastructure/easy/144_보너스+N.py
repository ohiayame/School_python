# `min(점수 + n, 100)` 으로 한 번에 clip 할 수 있습니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
n = int(input())

# 각 학생의 점수에 N을 더하되 100을 넘기지 않게 자른(clip) 결과를
# 이름: 새점수 형식으로 한 줄씩 dict 삽입 순서대로 출력
for name, score in scores.items():
    print(f"{name}: {min(score + n, 100)}")