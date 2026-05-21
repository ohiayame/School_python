# 빈 dict를 만든 뒤 `d[key] = value` 형태로 새 항목을 추가하세요.
# dict 순회 순서는 삽입 순서와 동일합니다.
n = int(input())

students = {}  # 변수명을 더 직관적으로 변경

# 1단계: 학생 정보를 dict에 등록
for _ in range(n):
    name = input()        # 이름 입력 받기
    score = int(input())  # 점수 입력 받기
    students[name] = score  # `d[key] = value` 형태로 새 항목을 추가

# 2단계: 등록된 학생을 이름: 점수 형식으로 출력 (등록 후 출력으로 단계 분리)
for name, score in students.items():
    print(f"{name}: {score}")