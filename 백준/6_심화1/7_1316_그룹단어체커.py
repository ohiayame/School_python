inputnum = int(input())
li = []
test = []
count = 0
for i in range(inputnum):
    inputmsg = input()
    li.append(inputmsg)
for i in li:
    char = list(m for m in i)
    check = char[0]
    flag = False
    for j in char:
        if check == j:
            for n in test:
                if n == j:
                    flag = True
                    count += 1
            if flag:
                test.append(j)
            else:
                pass
        else:
            check = j
    test = []
print(inputnum - count)