li = []


while True:
    num1, num2 = map(int,input().split())
    if num1 == 0 and num2 == 0:
        break
    
    factor = num1 % num2
    multiple = num2 % num1
    
    if factor == 0:
        li.append("multiple")
    elif multiple == 0:
        li.append("factor")
    else:
        li.append("neither")

for i in li:
    print(i)