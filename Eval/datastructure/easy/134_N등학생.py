# (점수, 이름) tuple 리스트로 묶어 sort(reverse=True) 후 N-1 인덱스로 접근.
names  = ["윤서", "지우", "민준", "서윤", "도윤"]
scores = [85, 92, 65, 78, 95]
rank = int(input())  # 변수명을 rank로 변경 — 등수(순위)임을 명확히 표현

# (점수, 이름) tuple 리스트로 내림차순 정렬
# zip 순서와 컴프리헨션 언패킹 순서를 일치시켜 가독성 향상
score_names = sorted([(score, name) for score, name in zip(scores, names)], reverse=True)

# N등 학생을 이름: 점수 형식으로 출력
score, name = score_names[rank - 1]
print(f"{name}: {score}")