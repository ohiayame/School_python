# keyword argument
def foo(arg_1, arg_2, arg_3):
    print(arg_1, arg_2, arg_3)
foo(arg_3 = 1, arg_2 = 2, arg_1 = 3)


# default argument
li = [5, 6, 7, 8]
def kin(arg_1 = 1, arg_2 = 2, arg_3 = 3, arg_4 = 4):
    print(arg_1, arg_2, arg_3, arg_4)
kin()
kin(6, 7, 8, 9)
kin(6)
kin(6, 7)
kin(6, 7, arg_4 = 10)
kin(int(input()))
kin(*li)
print(*li, sep='')



# 구구단
def gugu(value, num):
    for i in range(value, (value + 1) if num == None else (num + 1)) :
        for j in range(1,10):
            print(f"{i} x {j} = {value * j}")

gugu(2, 5)
gugu(3)


# variable parameter
# 1) *
# 2) **
# TUPLE로 변환

def foo(*args):
    print(len(args))
    for value in args:
        print(value)
foo(1)
foo(1, 2 ,3, 4 ,5 ,6 ,7 ,8 ,9 ,10 )

######
def foo(**args):
    print(len(args))
    for key, value in args.items():
        print(key,value)
    for  num in args.values():
        print(num)
    for keys in args.keys():
        print(keys)
    
foo(test = 2, king = 3)


######
def bar(*args):
    if len(args) == 1:
        start = end = args[0]
    elif len(args) == 2:
        start, end = args
    else :
        return
    for dan in range(start, end + 1):
        for num in range(1, 10):
            print(f"{dan} x {num} = {dan * num}")
bar(2)
bar(2, 3)    

######
# 앞에 있는걸 빼고 tuple로 변환  
def foo(arg , arg_, *args):
    print(len(args))
    for value in args:
        print(value, end = "")

foo(1, 2 ,3, 4 ,5 ,6 ,7 ,8 ,9 ,10 )

#####
def foo(arg_1, arg_2, arg_3):
    print(arg_1, arg_2, arg_3)

li = [1, 2, 3]
foo(*li)