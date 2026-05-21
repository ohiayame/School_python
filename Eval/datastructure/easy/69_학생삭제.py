# 항목 삭제는 `del d[key]` 또는 `d.pop(key)` 로 가능합니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()
# 입력된 학생은 항상 dict에 존재한다고 가정
# 해당 학생을 삭제
del scores[name]

# 남은 학생을 이름: 점수 형식으로 한 줄씩 출력
for name, score in scores.items():
    print(f"{name}: {score}")