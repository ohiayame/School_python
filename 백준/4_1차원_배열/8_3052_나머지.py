li = []
for i in range(10):
    input_value = int(input())
    num = input_value % 42 

    check = True
    for char in li:
        if char == num :
            check = False
    if check:
        li.append(num % 42)
count = 0
for _ in li:
    count += 1
print(count)