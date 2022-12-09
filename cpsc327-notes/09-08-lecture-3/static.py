class MyClass:
    # static variable: declare with class scope
    static_variable = 0

    def __init__(self, x):                          # instance method
        self.instance_variable = x
        MyClass.static_variable += 1

    def method(self):                               # instance method
        self.instance_variable += 1
        return 'instance method called', self, self.instance_variable

    @classmethod    # tells compiler to populate name of the class as "cls"
    def classmethod(cls):                           # class method
        cls.class_variable = 10                     # class variable
        return 'class method called', cls, cls.class_variable

    @staticmethod   # tells compiler to not ask for "self"
    def staticmethod():                             # static method
        MyClass.class_variable = 20                 # get class variable with Class in front
        # note that static method does not even know the name of the class; we have to specify MyClass instead of using cls
        return 'static method called', MyClass.class_variable   




if __name__ == "__main__":
    obj1 = MyClass(10)

    print(MyClass.static_variable)          # get static variable using Class in front
    print(obj1.instance_variable)
    # Output:
    # 1
    # 10

    obj2 = MyClass(20)

    print(MyClass.static_variable)
    print(obj2.instance_variable)
    # Output:
    # 2
    # 20

    print(obj1.method())
    print(obj1.classmethod())           # can call class method and static method from object instance
    print(obj1.staticmethod())
    print(MyClass.staticmethod())       # or call them from Class
    # Output:
    # ('instance method called', <__main__.MyClass object at 0x0000023FEB662220>, 11)
    # ('class method called', <class '__main__.MyClass'>, 10)
    # ('static method called', 20)
    # ('static method called', 20)
