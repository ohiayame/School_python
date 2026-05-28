# 조건 표현식을 dict comp 값 자리에 두고, zip 으로 짝 지어 순회하세요.
names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [100, 55, 72],
    [85],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# dict 컴프리헨션으로 {이름: 등급} 딕셔너리를 한 번에 생성
grades = {
    name: ('A' if s >= 90 else 'B' if s >= 80 else 'C' if s >= 70 else 'F')  # 조건 표현식 체이닝으로 등급 결정
    for name, s in zip(names, scores)  # zip으로 이름과 점수를 짝지어 순회
}

# dict.items()로 순회하여 출력
for k, v in grades.items():
    print(f"{k}: {v}")