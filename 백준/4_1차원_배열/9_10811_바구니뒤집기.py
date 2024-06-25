n, m = map(int,input().split())
li = []
for i in range(1, n+1):
    li.append(i)
for _ in range(m):
    i,j = map(int,input().split())
    i -= 1
    # if j == n:
    #     j = -1
    # else:
    #     pass
    num = li[i:j]
    # count = 1
    # for num2 in num:
    #     li.insert(i,num2)
    #     li.pop(i + count)
    #     count += 1
    num.reverse()
    li[i:j] = num
for value in li:
    print(value, end = " ")