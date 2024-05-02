import sys
num = int(sys.stdin.readline())
li = []
for _ in range(num):
    a, b = map (int, sys.stdin.readline().split())
    li.append(a + b)

count = 0
for i in li:
    count += 1
    print(f"Case #{count}: {i}")