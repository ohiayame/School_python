inputnum = int(input())
li = []
outli = []
# input for msg 
for i in range(inputnum):
    inputmsg = input()
    li.append(inputmsg)
    
for i in li:
    char = list(m for m in i)
    outflag = True
    count = 0
    test = []
    for j in char:
        if not outflag:
            break
        for n in test:
            if n == j:
                if n != test[-1]:
                    outflag = False
                    outli.append(i)
                break
        if outflag:
            test.append(j)
                

print(len(li) - len(outli))