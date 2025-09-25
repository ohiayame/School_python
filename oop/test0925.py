class A:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"
    def prt(self):
        print(self.__private)
obj = A()
print(obj.__dict__)
# -> # {'public': 'public', '_protected': 'protected', '_A__private': 'private'}

obj.prt()
# print(obj.public) 
# print(obj._protected)
# print(obj.__private)    
# AttributeError: 'A' object has no attribute '__private'. Did you mean: '_A__private'?

