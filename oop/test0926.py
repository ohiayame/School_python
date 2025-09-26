# class Bar:
#     def __init__(self):
#         self._name = "bar"

# class Foo(Bar):
#     def __init__(self):
#         super().__init__()
#         self.name= "foo"
        
# obj = Foo()
# print(obj.__dict__) 
#  # {'_name ': 'bar', 'name': 'foo'}  



# class A:
#     def __init__(self):
#         self.__age = None
    
#     @property
#     def age(self):
#         return f"나이는 : {self.__age}"

#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise TypeError("음수")
#         self.__age = age

# obj = A()
# obj.age = 10
# print(obj.age)
# obj.age = -10



# 위치 인자 (Positional Arguments)
# 키워드 인자 (Keyword Arguments)
# def calculate(x, y, /, op="+"):
#     if op == "+":
#         print(x + y)
#     elif op == "-":
#         print(x - y)
#     else:
#         print("error")

# calculate(y=2, x=5)
# calculate(y=10, x=20, "-") 

# 가변 위치 인자 (*args)
# def prt(a, *arg):
#     print(a, arg)

# prt(1)
# prt(1, 2)
# prt(1, 2, 3)

# def prt(**arg):
#     for key, value in arg.items():
#         print(f"{key}, {value}")
    
# prt(d=3, test="ddd")

def prt(a, *b, c= 10, d=20, **kwargs):
    print(a, b, c, d, kwargs)
prt(1, 2, 3, 4, 5, op=200, d=100)