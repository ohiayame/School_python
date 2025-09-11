class Foo:
    # class method
    @classmethod
    def class_method(cls, age):
        cls.age = age
    
    # instance
    def instance_method(self, age):
        self.age = age
    
obj = Foo()
obj.class_method(30)     # class_method(Foo, 30)
obj.instance_method(100) # instance_method(obj, 100)

print(Foo.age, obj.age)
