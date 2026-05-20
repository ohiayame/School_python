# 컴프리헨션 한 줄로 새 리스트를 만든 뒤 출력하세요.
data_sets = [
    [1, 2, 3, 4, 5, 6, 7],
    [10, 20, 30],
    [0],
]

t = int(input())
nums = data_sets[t]

# 각 원소를 제곱한 새 리스트를 만들고, 공백 구분으로 한 줄에 출력
squared_nums = [num ** 2 for num in nums]  # 변수명을 내용에 맞게 squared_nums 로 변경

print(" ".join(str(val) for val in squared_nums))