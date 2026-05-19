# 음수 인덱스를 사용하면 뒤에서부터 접근할 수 있습니다.
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤", "예준"],
    ["red", "green", "blue"],
    ["혼자"],
]
t = int(input())
names = data_sets[t]

# data_sets의 t번째 배열의 0번째와 -1(마지막) 원소 출력
print(f"첫 번째: {names[0]}")
print(f"마지막: {names[-1]}")