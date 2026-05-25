# `scores.values()` 를 순회하며 cutoff 이상인 값의 개수를 세세요.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# 점수가 cutoff 이상인 학생 수
print(sum(1 for score in scores.values() if score >= cutoff))