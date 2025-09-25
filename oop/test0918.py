# class Parent:
#     def prt_name(self):
#         print(self.name)
    

# class Child (Parent):
#     def __init__(self):
#         self.name = "Child"

# obj = Child()
# obj.prt_name()
class Kin():
    pass
class Bar:
    def __init__(self):
        self.name = "YC Jung"

    def prt_info(self):
        print(self.name, self.age)

class Foo(Bar, Kin):
    def __init__(self):
        self.age = "18"
        super().__init__()

print(Foo.mro())
obj = Foo()
# obj.prt_info()