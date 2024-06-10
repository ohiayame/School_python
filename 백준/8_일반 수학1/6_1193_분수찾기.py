num = int(input())
naname = 1
while num > naname:
    num -= naname
    naname += 1

if naname % 2 == 0:
    x = num
    y = naname + 1 - x
else:
    y = num
    x = naname + 1 - y
print(f"{x}/{y}")