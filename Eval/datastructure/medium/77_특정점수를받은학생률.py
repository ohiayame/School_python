# items()로 (이름, 점수)를 순회하면서 일치하는 이름만 모아 출력하세요.
scores = {"윤서": 85, "지우": 92, "민준": 85, "서윤": 78, "도윤": 92, "예준": 65}
target_score = int(input())  # 변수명을 target_score로 변경해 의도를 명확히 표현

# 같은 점수의 학생 이름을 저장
match_names = [name for name, student_score in scores.items() if student_score == target_score]

# 같은 점수인 학생이 있으면 이름 출력 / 없으면 없음 출력
if match_names:  # len() > 0 대신 truthy 체크로 더 Pythonic하게
    print(*match_names)
else:
    print("없음")