class Bird():
    def fly(self):
        raise NotImplementedError()

class Duck(Bird):
    def fly(self):
        print("Duck flying")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")


class Whale():
    def swim(self):
        print("Whale swimming")


animals = [Duck(), Sparrow(), Whale()]      # python: lists can have different types
for animal in animals:
    animal.fly()


# Will lead to error: AttributeError: 'Whale' object has no attribute 'fly'
# No compile error, just this runtime error

# If we add a fly() method to Whale class, it will run without error
# even though Whale has no connection to Bird; python doesn't care
