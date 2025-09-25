class Bar:
    def i_method(self):
        self.iValue = 20

    @classmethod
    def c_method(cls):
        cls.cValue = 30
    
    # @staticmethod
    # def s_method():
    #     print("Static method")

obj = Bar()
obj.i_method()
Bar.i_method(obj)
obj.c_method()

# obj.s_method()
# Bar.s_method()

del Bar.cValue

Bar.cValue = 10000
# print(Bar.cValue)


class Foo:
    def __init__(self, id):
        self.id = id
        print(f"Constructor of object {self.id} is invoked")
    def __del__(self):
        print(f"Destructor of object {self.id} is invoked")

obj1 = Foo(1)
obj2 = Foo(2)
del obj1
print("Program is terminated")
del obj2