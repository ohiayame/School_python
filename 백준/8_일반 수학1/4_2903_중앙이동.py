input_num = int(input())
num = 3

if input_num == 1:
    num = 3 ** 2
else:
    tohagi = 1
    for _ in range(input_num - 1):
        tohagi *= 2
        num += tohagi
    
print(num ** 2)
print(num)