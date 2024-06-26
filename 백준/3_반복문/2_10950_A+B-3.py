count = int(input())
li = []
for _ in range(count):
    num1, num2 = map(int,input().split())
    li.append(num1 + num2)
    
for num in li:
    print(num) 