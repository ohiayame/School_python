input_msg = input()
li = []
revers = []

for char in input_msg:
    li.append(char)
for re in li[-1:0:-1]:
    revers.append(re)
revers.append(li[0])

flag = len(li)
for i in range(len(li)):
    if revers[i] == li[i]:
        flag -= 1
if flag == 0:
    print(1)
else:
    print(0)