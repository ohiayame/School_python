# class Foo:
#     name = "Class member variable: Foo"
#     def test(instance_ref):
#         instance_ref.name = "Instance member variable: Foo"

# obj = Foo()
# obj.test()

# print(obj.name)
# print(Foo.name)


class Foo:
    # 생성자에서 미리 사용할 변수를 정의
    def __init__(self):
        self.name = ""
        self.aeg = ""
        
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age

obj = Foo()

obj.set_name("Name")
print(obj.name)
del obj.name
print(obj.name)