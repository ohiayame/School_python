# 짝수 판별: 2로 나눈 나머지가 0.
data_sets = [
    [1, 4, 7, 2, 9, 6, 3, 8, 10, 5],
    [1, 2, 3, 4, 5],
    [1, 3, 5, 7, 9],
]
t = int(input())
data = data_sets[t]

# 리스트 컴프리헨션으로 짝수만 추출해 공백 구분으로 한 줄에 출력
even_nums = [num for num in data if num % 2 == 0]
print(" ".join(map(str, even_nums)))