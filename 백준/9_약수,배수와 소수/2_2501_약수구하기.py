inputnum1, inputnum2 = map(int, input().split())

li = []
num = 0

while len(li) < inputnum2:
    num += 1
    if (inputnum1 % num == 0):
        li.append(num)
    if num == inputnum1:
        break

if len(li) < inputnum2:
    li.append(0)
print(li[-1])