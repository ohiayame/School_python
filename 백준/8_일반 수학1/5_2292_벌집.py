num = 1
input_num = int(input())
cou = 1
allnum = 1
for i in range(1,1000000000):
    if input_num <= allnum:
        break
    else:
        num = i * 6
        cou += 1
        allnum += num
print(cou)