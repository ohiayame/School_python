# A가 B보다 큰 경우에는 '>'를 출력한다. 
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.

a,b = map(int,input().split())

msg = ""
if a > b:
    msg = ">"    
elif a < b :
    msg = "<"
else:
    msg ="=="
    
print(msg)