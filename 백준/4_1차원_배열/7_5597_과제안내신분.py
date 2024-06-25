li = []

for i in range(1,31):
    li.append(i)
for _ in range(28):
    input_num = int(input())
    li.remove(input_num)

for num in li:
    print(num)