m, n = map(int,input().split())
li = []
for i in range(m):
    li.append(0)
for _ in range(n):
    i,j,k = map(int,input().split())

    for num in range(i-1, j):
       li[num] = k
for num in li:
    print(num,end = " ")