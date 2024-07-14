import os

f_handler_1 = open("score.txt","r+", encoding= "utf-8")
msg = f_handler_1.read()
count = 0
m = ""
for line in msg:
    if line == "\n":
        print(m)
        m = ""
    else:
        m += line

f_handler_1.close()
