num = int(input())
for value in range(1,num + 1):
    clear = " " * (num - value)
    print(f'{clear}{"*" * value}') 