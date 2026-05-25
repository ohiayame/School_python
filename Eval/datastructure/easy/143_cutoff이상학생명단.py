# `for name, s in scores.items():` 순회하며 조건 만족하는 이름을 모으세요.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# 정수 cutoff를 한 줄로 입력받아, 점수가 cutoff 이상인 학생 이름을
# dict 삽입 순서대로 공백 구분으로 한 줄에 출력
result = [name for name, score in scores.items() if score >= cutoff]  # 필터링 결과 리스트
print(" ".join(result))