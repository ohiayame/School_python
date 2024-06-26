# Quarter, $0.25 
# Dime, $0.10
# Nickel, $0.05
# Penny, $0.01
num = int(input())
li_ = [] 
for _ in range(num):
    value = int(input())
    li = [0, 0, 0, 0]
    
    if value >= 25:
        q = value // 25
        value = value % 25
        li[0] = q
    if value >= 10:
        d = value // 10
        value = value % 10
        li[1] = d
    if value >= 5:
        n = value // 5
        value = value % 5
        li[2] = n
    if value >= 1:
        li[3] = value
    li_.append(li)
for i in li_:
    for j in i:
        print(j,end = " ")
        
    print()

###########
n = int(input())

for _ in range(n):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money//i, end=' ')
		money = money%i