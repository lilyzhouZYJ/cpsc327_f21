class MyClass:
    def __init__(self):
        self._instance_var = 2
    
    @staticmethod
    def staticMethod(self):
        print(self._instance_var)

class Example:
    def __init__(self, names=[]):
        self.names = names
    
a = Example()
b = Example()
c = Example(["Sherry"])

a.names.append("Tim")

print(a.names, b.names, c.names)