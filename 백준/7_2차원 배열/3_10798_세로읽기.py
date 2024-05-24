li_1 = []
li_2 = []
li_3 = []
li_4 = []
li_5 = []
for _ in range(5):
    char = str(input())
    for i in char:
        if _ == 0:
            li_1.append(i)
        if _ == 1:
            li_2.append(i)
        if _ == 2:
            li_3.append(i)
        if _ == 3:
            li_4.append(i)
        if _ == 4:
            li_5.append(i)
msg = ""
for i in range(15):
    if i < len(li_1):
        msg += str(li_1[i])
    if i < len(li_2):
        msg += str(li_2[i])
    if i < len(li_3):
        msg += str(li_3[i])
    if i < len(li_4):
        msg += str(li_4[i])
    if i < len(li_5):
        msg += str(li_5[i])
print(msg)