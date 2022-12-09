class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        print("Calling method on Left Subclass")
        BaseClass.call_me(self)
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        print("Calling method on Right Subclass")
        BaseClass.call_me(self)
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    def call_me(self):
        print("Calling method on Subclass")
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)



s = Subclass()
print(Subclass.__mro__)
# Subclass, LeftSubclass, RightSubclass, BasClass, Object

s.call_me()
# Output:
# Calling method on Subclass
# Calling method on Left Subclass
# Calling method on Base Class
# Calling method on Right Subclass
# Calling method on Base Class

print(s.num_base_calls)
# 2