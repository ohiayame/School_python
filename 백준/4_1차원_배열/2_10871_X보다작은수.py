a, b = map(int,input().split())
input_value = map(int,input().split())
li =[]
for i in input_value:
    if i < b:
        li.append(i)
        print(i ,end = " ")