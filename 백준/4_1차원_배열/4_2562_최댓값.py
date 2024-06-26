max = 0
num = 0 
for i in range(1,10):
    value = int(input())
    if value > max:
        max = value
        num = i
print(max)
print(num) 