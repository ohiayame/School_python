msg = "프로그램 시작"
print(msg)

def bar(argB1, argB2):
    msg1 = "안녕!" + foo(argB1)
    print(msg1)
    
    msg2 = "안녕!" + foo(argB2)
    print(msg2)
    
def foo(argF) :
    msg = argF + "님"
    msg = pos(msg)   
    return msg

def pos(argP):
    msg = "*" + argP + "*"
    return msg

bar("정영철","YC JUNG")

msg = "프로그램 종료"
print(msg)