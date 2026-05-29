# update() 의 결과는 None — main 이 직접 변경됩니다.
main_sets = [
    {"수학": 80, "영어": 75, "과학": 90},
    {"A": 1, "B": 2},
    {"X": 10, "Y": 20},
]
update_sets = [
    {"영어": 88, "역사": 70},
    {"C": 3, "D": 4},
    {},
]
t = int(input())
main = main_sets[t]
update_data = update_sets[t]

# update 진행
main.update(update_data)

# update한 데이터를 키: 값 형식으로 한 줄씩 출력
for name, score in main.items():
    print(f"{name}: {score}")