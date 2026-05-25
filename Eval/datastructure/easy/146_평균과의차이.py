# 평균을 먼저 계산, `abs(scores[name] - avg)` 를 f-string `:.1f` 로 포맷.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 평균 계산
avg = sum(scores.values()) / len(scores)

if name not in scores:
    print("해당 학생을 찾을 수 없습니다.")
else:
    # abs(scores[name] - avg)` 를 f-string `:.1f` 로 포맷.
    print(f"차이: {abs(scores[name] - avg):.1f}")