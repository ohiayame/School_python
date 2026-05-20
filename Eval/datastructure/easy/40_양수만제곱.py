# 표현식과 if 조건을 함께 사용.
data_sets = [
    [3, -1, 0, 7, -5, 2, -8, 4],
    [10, -5, 20, 0],
    [-1, -2, -3],
]
t = int(input())
data = data_sets[t]

# 리스트 컴프리헨션으로 양수(> 0)만 골라 제곱한 결과를 공백 구분으로 한 줄에 출력
squared_positives = [num ** 2 for num in data if num > 0]
print(" ".join(map(str, squared_positives)))