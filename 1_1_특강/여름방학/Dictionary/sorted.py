bar = [1, 10, 5, 2, 9]

result = sorted(bar, reverse=True)
print(result)   # [10, 9, 5, 2, 1]

result = sorted(bar, reverse=False)
print(result)   # [1, 2, 5, 9, 10]



# 2차원 리스트
bar = [[10, 9],
    [2, 8],
    [3, 10]
]

# 첫 번째 index을 기준
result = sorted(bar, reverse=True)
print(result)   # [[10, 9], [3, 10], [2, 8]]

result = sorted(bar, reverse=False)
print(result)   # [[2, 8], [3, 10], [10, 9]]

# 두 번째 index을 기준
def get_value(recode):
    print(recode)
    return(recode[1])
result = sorted(bar, key= get_value, reverse=True)
print(result)   # [[3, 10], [10, 9], [2, 8]]

result = sorted(bar, key= lambda recode : recode[1], reverse=False)
print(result)   # [[2, 8], [10, 9], [3, 10]]