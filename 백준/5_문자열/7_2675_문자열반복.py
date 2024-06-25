num = int(input())
li = []
for i in range(num):
    count, char = input().split()
    msg = ""
    for chr in char:
        msg += chr * int(count)
    li.append(msg)
for text in li:
    print(text, end = "")
    print()