input_num = int(input())
naname = 1

while input_num > naname:
    input_num -= naname
    naname += 1
    
if naname % 2 == 0:
    x = naname + 1 - input_num
    y = input_num
else:
    y = naname + 1 - input_num
    x = input_num
    
print(f"{y}/{x}")