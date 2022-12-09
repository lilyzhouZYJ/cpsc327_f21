# 09-20 Lecture 6

## Lecture Today

- More examples of mixins and multiple inheritance
- Abstract classes and interfaces
- Python/Java/C++ comparisons
- **Moving on to chapter 4...**

<br>

## Mixins

- Specific use case for multiple inheritance
- Not meant to be used on their own (i.e. no instances of their own)
- Add features to multiple other classes
  - Careful about name collisions
- Composition is an alternative

*Examples (from last-lecture directory)*:
- [students.py](./../09-15-lecture-5/students.py): the `ULA` class inherits from both `Lecturer` and `Student`
- [composition.py](./../09-15-lecture-5/composition.py): demonstrates how inheritance (and multiple inheritance) can be achieved with composition
- [mixin.py](../09-15-lecture-5/mixin.py): bringing in functionalities from mixins

<br>

## Abstract Classes and Interfaces

- Not meant to be instantiated directly
  - Similar to mixins in this sense
- Serves as a template for other classes
- *Example*:
  - We can have `StudentDriver` and `AdultDriver` inherit from `Driver`
  - But there is no reason we would ever instantiate a `Driver` object
    - Just an abstract class, template for building `StudentDriver` and `AdultDriver`
- Defines the public interface, for subclasses
- Typically does not implement methods
  - Defines the methods that subclasses should have; but does not implement them
  - Requires subclasses to implement them
- Important in statically typed languages where polymorphism is necessary to work on different types that implement the same interface
- Not a core feature of Python
  - Still useful to structure/organize code and make it harder to forget to implement part of the interface

### **Python**

*Example*:
- [audio_play.py](./audio_player.py): enforcing abstract classes using `abc`
- [abstract_classes.py](./abstract_classes.py)

### **Java**

- Abstract classes and interfaces
  - Very similar, but interfaces are more restricted
- No multiple inheritance, but can implement more than one interface
  - Interfaces with no implementations => would not have the issue of conflicting implementations
- Now Java allows interface with default method implementations:
  - Have to explicitly call `InterfaceName.super.methodCall()` to resolve conflicts
- Has `super` like Python, but cannot "skip a level"

*Example*: 
- [abstract_classes.java](./abstract_classes.java)
- [interfaces.java](./interfaces.java)

### **C++**

- More similar to Python
- No explicit abstract classes or interfaces
  - Create a **pure virtual function**
  - Compile error if such functions are used without overriding first
- Supports multiple inheritance
  - Compile error if ambiguous, like the diamond problem
- No `super`
  - Diamond problem resolved with **virtual inheritance**
  - Can choose correct parent method with `::` operator

*Example*: [abstract_classes.cpp](./abstract_classes.cpp)

<br>

## More on Multiple Inheritance: Diamond Problem

- [bad_mi.py](./bad_mi.py): example of bad multiple inheritance
- [super_mi.py](./super_mi.py): example of good multiple inheritance, using `super`
  - Allows the diamond problem to be resolved by the MRO
