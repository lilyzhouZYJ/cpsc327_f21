
# Examples of changing function attribute:

def my_function():
    print("The function was called")

my_function.description = "A silly function"
print(dir(my_function))
print(my_function)


def second_function():
    print("The second function was called")

second_function.description = "A sillier function."




def another_function(function):
    print("The description:", end=" ")
    print(function.description)             # description of function
    print("The name:", end=" ")
    print(function.__name__)                # name of function
    print("The class:", end=" ")
    print(function.__class__)               # class of function
    print("Now I'll call the function passed in")
    function()



class ClassA:
    def foo(self):
        print("Called foo")

another_function(my_function)
another_function(second_function)

a = ClassA()
b = ClassA()

print(a.foo)
print(b.foo)

