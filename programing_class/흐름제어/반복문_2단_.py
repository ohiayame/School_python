for i in range(1,3):
    for j in range(1, 4):
        if i == 2:
            break
        print(i ,":", j)

for i in range(4):
    for j in range(3):
        print("*",end = "")
    print()

for k in range(1,5):
    for i in range(1,3):
        for j in range(1, 4):
            if i == 2:
                break
            print(i ,":", j)