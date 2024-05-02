import sys
li = []
while True:

    a, b = map (int, sys.stdin.readline().split())
    
    if a == 0 and b == 0:
        break
    else:
        li.append(a + b)
    
for sum in li:
    print(sum)
    