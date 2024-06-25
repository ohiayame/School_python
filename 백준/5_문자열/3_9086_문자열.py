num = int(input())
li = []
for i in range(num):
    msg = input()
    li.append(msg[0])
    li.append(msg[-1])
message = ""
count = 0
for char in li:   
    message += char
    count += 1
    if count == 2:
        print(message)
        message = ""
        count = 0