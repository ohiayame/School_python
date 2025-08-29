class Foo:
    # member variable
    # class MV
    age = 20
    name = "YC Jung"
    
    # 생성자
    # 메직메서드 -> __ 시작
    def __init__(self, name, age):
        # instance MV
        self.name = name
        self.age = age

# obj = Foo("YC", 40)
# print(Foo.age)
# print(obj.age)

# 단일 상속
class Parent:
    pass

class Child(Parent):
    pass

# 다중 상속 지원
class A:
    pass

class B:
    pass

class C(A, B):
    pass


class Bar:
    def __init__(self):
        self.x = 10
    def test(self):
        self.y = 20

obj = Bar()
print(obj.x)

obj.test()
print(obj.y)
Bar.d = 100
print(Bar.d)
print(obj.d)
obj.z = 1
print(obj.z)
