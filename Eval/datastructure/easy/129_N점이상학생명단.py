# zip 또는 인덱스 순회로 (이름, 점수) 쌍을 보면서 조건 만족하는 이름만 모으세요.
names  = ["윤서", "지우", "민준", "서윤", "도윤"]
scores = [85, 92, 65, 78, 95]
min_score = int(input())

# 점수가 min_score 이상인 학생 이름을 입력 순서대로 공백 구분으로 한 줄에 출력
print(" ".join(name for name, score in zip(names, scores) if score >= min_score))