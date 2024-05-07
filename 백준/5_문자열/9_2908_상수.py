a, b = input().split()
li1 = []
li2 = []
for i in a:
    li1.insert(0, i)
A = ""
for i in li1:
    A += i

for i in b:
    li2.insert(0, i)
B = ""
for i in li2:
    B += i
if A >= B:
    print(A)
else :
    print(B)