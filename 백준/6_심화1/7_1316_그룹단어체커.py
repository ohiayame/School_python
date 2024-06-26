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

#############
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)