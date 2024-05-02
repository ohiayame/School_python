value = int(input())
max_value = 0
li = []


num = map(int, input().split())
for num1 in num:
    li.append(num1)
    
max_value = max(li)
all_value = 0

for i in li:
    number = int(i)/max_value*100
    all_value += number


print(all_value/value)