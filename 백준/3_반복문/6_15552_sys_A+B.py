import sys
num = int(sys.stdin.readline())
li = []
for _ in range(num):
    a, b = map (int, sys.stdin.readline().split())
    li.append(a + b)
    
for sum in li:
    print(sum)