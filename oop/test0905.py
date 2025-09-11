class Bar:
    name = "YC Jung"
    
    def __init__(self):
        self.age = 20
    
    def hello(self):
        print(self.name)

# obj = Bar()
# obj.hello()


# --------------------------

class Foo:
    univ = "YJU"
    
    def __init__(self, name):
        self.name = name
    
    def prt_info(self, age):
        self.age = age
        print(self.name, self.age)

obj1 = Foo("Kin")
obj1.prt_info("20")
obj2 = Foo("Hong")
obj2.prt_info("30")