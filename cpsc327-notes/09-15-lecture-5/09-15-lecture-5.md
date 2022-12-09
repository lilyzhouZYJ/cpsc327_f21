# 09-15 Lecture 5

## Lecture Today

- Basic inheritance
- Extending built-in classes
- Multiple inheritance
- More about `super`

<br>

## Basic Inheritance

- Child class inherits:
  - Instance variables
  - Instance methods
  - Existing relationships are included
  - Only inherit `public` or `protected` attributes in other languages
    - (A newly added subclass is considered an external class.)
    - Python: doesn't enforce private => everything is inherited
- Hierarchical relationships:
  - Any shared code (data and behaviors) belongs in the parent
  - Subclass specializes
    - Add new variables/methods
    - Modify existing variables/methods
- What code goes in which class is all about the **model**
- All classes inherit from `Objects` by default

*Example*: [courses.py](./courses.py)

<br>

## Using/Overriding Parent Class

- `super()`
  - Same as `super(CurrentClass, self)`
  - Can skip hierarchy level using `super(ParentClass, self)`
    - `ParentClass` is where we start looking first
- Reuse a method *specifically from a parent*
  - Avoiding name clashes
  - `super` is generally not needed to use a parent's methods (since they are already inherited in `self`)
- Often needed in `__init__`, but may also be used elsewhere
- May appear anywhere in a method

<br>

## Extending Built-In Classes

```python
# inherit the built-in list
class ContactList(list):
    def search(self, name):
        ...

all_contacts = ContactList()
all_contacts.append(Contact("Tim","timothy@yale.edu"))  # "append" from list
print(all_contacts[0])  # "__getattr__" from list
```

<br>

## Multiple Inheritance

- One class inherits from multiple others
  - `class MyClass(ClassA, ClassB, ...)`
- Get all the attributes and behaviors of all parent classes
- What if there are conflicts?
  - `super()` can help out
  - Best to avoid conflicts
- Composition is an alternative

*Example*:
- [students.py](./students.py): the `ULA` class inherits from both `Lecturer` and `Student`
- [composition.py](./composition.py): demonstrates how inheritance (and multiple inheritance) can be achieved with composition
  - We can create ULA objects by giving both `learner` and `teacher` attributes to the Person object

### **Diamond Problem**

```python
class BaseClass:
  def call_me()

class LeftSubclass(BaseClass):
  def call_me():
    BaseClass.call_me()

class RightSubclass(BaseClass):
  def call_me():
    BaseClass.call_me()

class Subclass(LeftSubclass, RightSubclass):
  def call_me():
    LeftSubclass.call_me(self)
    RightSubclass.call_me(self)

# problem: 
# The call_me of Subclass would call BaseClass.call_me() twice, 
# which might not be what we want.
```

- Solution: use `super`
  - **Method resolution order (MRO)**: default order of classes in which we look for the method called

### **Mixin**

- Specific use case for multiple inheritance
- Mixins are not meant to be used on their own
- To bring in features to other classes
  - Careful about collisions

*Example*: [comparable.py](./comparable.py)
- `ComparableMixin` class:
  - Expects a class to implement `__lt__`
  - Will implement all the other comparison dunder methods