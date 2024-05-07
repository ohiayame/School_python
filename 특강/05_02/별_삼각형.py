num = int(input("count number: "))
for value in range(1,num + 1):
    clear = " " * (num - value)
    value = "*" * (value * 2 - 1)
    print(f'{clear}{value}')