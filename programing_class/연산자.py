# bar = 30
# bar, foo, kin = 10, 20, 30
# print(f"{bar}, {foo}, {kin}")

# def getValue():
#     return 2, 3, 4, 5
# print(getValue())
# print(type(getValue()))

# bar = [2, 3, 4, 5]  # list
# foo = (6, 7, 8, 9)  # tuple
# print(bar[0])
# print(foo[0])
# bar[0] = 20
# foo[0] = 60

# bar = foo = kin = 2
# print(bar, foo, kin)

# bar = "hello"
# for char in bar :
#     print(char, end ="")
# print()
# for char in (foo := "world"):
#     print(char, end = "")

# def getValue(argA, argB):
#     return(argA + argB, argA - argB, argA * argB, argA / argB)
# kin = getValue(2,3)
# foo = list(kin)
# foo[0] = foo[0] + 1
# print(foo[0])


# def myInvalue(argA, argB):
#     for i in argB:
#         if argA == i :
#             return False
#     return True  

# print("a" in "abc")

# bar = [3,4,5,6]
# print(4 in bar)
# print(4 not in bar)
# print(myInvalue (4, [2, 3, 4]))

bar = [2, 3, 4]
foo = [2, 3, 4]

if bar == foo :
    print("참")
else:
    print("거짓")
    
if bar is foo :
    print("참")
else:
    print("거짓")
    
print("참"if bar == (foo := list((2, 3, 4)))else "거짓")