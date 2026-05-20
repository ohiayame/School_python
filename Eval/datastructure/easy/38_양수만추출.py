# 컴프리헨션 한 줄로 필터링.
data_sets = [
    [3, -1, 0, 7, -5, 2, -8, 4],
    [-3, 10, -5, 20, 0],
    [-1, -2, 0, -3],
]
t = int(input())
data = data_sets[t]

# 리스트 컴프리헨션의 if 절을 사용해 양수(> 0)만 추출
positive_datas = [num for num in data if num > 0]

# 출력은 " ".join(str(x) for x in 결과) 사용
print(" ".join(str(val) for val in positive_datas))