# 빈 dict 의 길이는 0 입니다.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {},
]

# 시나리오 번호 입력받기
t = int(input())
scores = data_sets[t]

# dict 의 키 개수(등록된 학생 수)를 len()으로 구해 출력
print(f"총 {len(scores)}명")