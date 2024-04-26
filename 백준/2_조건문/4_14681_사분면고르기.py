x = int(input())
y = int(input())

msg = 0
if x > 0 and y > 0 :
    msg = 1
elif x < 0 and y > 0 :
    msg = 2
elif x < 0 and y < 0 :
    msg = 3
elif x > 0 and y < 0 :
    msg = 4
print(msg)