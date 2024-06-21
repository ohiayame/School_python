# li = []
# for i in range(9):
#     num = map(int,input().split())
#     for i in num:
#         li.append(i)
li = [list(map(int, input().split())) for _ in range(9)]
print(max(li))

index = li.index(max(li))
hen = index // 9 + 1
yoru = 10 - ( 9 - index % 9)
print(hen, yoru)