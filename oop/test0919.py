class A:
    def __init__(self):
        print("a")
    def prt(self):
        print("A")
class B(A):
    pass
    # def prt(self):
    #     print("B")
class C(A):
    def prt(self):
        print("C")

class D(B, C):
    def prt(self):
        print("D")
        super().prt()

obj = D()
print(D.mro())
obj.prt()


# class Parent:
#     def prt(self):
#         print(Parent)
# class Child(Parent):
#     def prt(self):
#         print("Child")

# obj = Child()
# obj.prt()