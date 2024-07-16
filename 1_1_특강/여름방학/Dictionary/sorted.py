# bar = [1, 10, 5, 2, 9]

# result = sorted(bar, reverse=True)
# print(result)   # [10, 9, 5, 2, 1]

# result = sorted(bar, reverse=False)
# print(result)   # [1, 2, 5, 9, 10]



# # 2차원 리스트
# bar = [[10, 9],
#     [2, 8],
#     [3, 10]
# ]

# # 첫 번째 index을 기준
# result = sorted(bar, reverse=True)
# print(result)   # [[10, 9], [3, 10], [2, 8]]

# result = sorted(bar, reverse=False)
# print(result)   # [[2, 8], [3, 10], [10, 9]]

# # 두 번째 index을 기준
# def get_value(recode):
#     print(recode)
#     return(recode[1])
# result = sorted(bar, key= get_value, reverse=True)
# print(result)   # [[3, 10], [10, 9], [2, 8]]

# result = sorted(bar, key= lambda recode : recode[1], reverse=False)
# print(result)   # [[2, 8], [10, 9], [3, 10]]




# import random

# # bar = random.sample(range(1, 100), 10)
# bar = [random.randint(1, 100) for _ in range(10)]

# print(bar)


# foo = [[[row + item + i for row in range(3)] for item in range(3)] for i in range(2)]


# # bar : [95, 56, 44, 100, 76, 29, 60, 90, 8, 93]
# result = sorted(bar)  # 복사본을 정렬    ### reverse를 설정 안하면 올라가(False) (내림순: True)

# print(bar) # [95, 56, 44, 100, 76, 29, 60, 90, 8, 93]
# print(result) # [8, 29, 44, 56, 60, 76, 90, 93, 95, 100]

# result = sorted(foo, reverse=True)
# print(result)


li = [
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [2,3,4]
    ],
    [
        [0,0,0],
        [0,0,0]
    ]
]

result = sorted(li)

result = sorted(li, key= lambda record : sum(record[1]), reverse=False)
print(result)




# # Sorting -> 정렬 -> 
# # 1) 오름차순 False　: 1, 2, 3, 4
# # 2) 내림차순 True　: 4, 3, 2, 1

# # 자료구조
# # 1차원 자료구조 -> List

# # 1 ~ 100사이 숫자 10개를 리스트에 저장하라.
# import random

# # Matrix
# bar = [
#         [
#             [13, 8],[55, 85] # 13
#         ],
#         [
#             [10, 20],[30, 40] # 10
#         ] ,
#         [
#             [40, 50],[60, 70] # 40
#         ] 
#     ]   

# def get_value(bar):
#     return sum([ item for record in bar for item in record])
#     # sum = 0
#     # for record in bar:
#     #     for item in record:
#     #         sum += item
#     # return sum


# result = sorted(bar,  key = get_value , reverse=True) 

# print(result) 

