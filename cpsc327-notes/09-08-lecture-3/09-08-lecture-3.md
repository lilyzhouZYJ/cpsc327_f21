# 09-08 Lecture 3

## Terminology Review

- Data in an object
  - Instance variables, instance data
  - Members - both data and methods, bound to instances of objects
  - Fields, attributes, properties
- Behaviors
  - Methods

<br>

## Lecture Today

- Revisiting `Point` class
- Organizing project modules and imports
- Docstring
- Instance/class/statis members
- Immutable/mutable defaults
- Getters/setters
- Notebook case-study

<br>

## Organizing a Project

- Each python file is a **module**:
  - `accounts.py` - a python module
- If everything is in one folder:
  - `import accounts` => then we can use `accounts.SavingsAccount()`
    - `accounts` is module, and `SavingsAccount` is a class in it.
  - `from accounts import SavingsAccount` => `SavingsAccount()`
  - `from accounts import *`
    - Not recommended; will have trouble finding which modules the stuff came from
  - `from accounts import SavingsAccount as sa` => `sa()`
  - Cannot do: `import accounts.SavingsAccount`
    - `SavingsAccount` is not a module
- **Packages**:
  - Package - folder of modules or packages
  - Every package has a `__init__.py`
    - This is how the compiler knows this is a package

### Example:

```python
sound/
    __init__.py
    formats/
        __init__.py
        wavread.py
        wavwrite.py
    effects/
        __init__.py
        echo.py       # contains method echofilter()
        surround.py
    filters/
        __init__.py
        equalizer.py
        karaoke.py

# option 1:
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# option 2:
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

# option 3:
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)

# cannot do:
import sound.effects.echo.echofilter    # because echofilter is not a module
```

<br>

### Relative Package Reference

If you are in `surround.py`:
- `from . import echo`
- `from .. import formats`
- `from ..filters import equalizer`

<br>

## Docstrings

- Document the purpose and behavior of objects and methods
- Describe the public interface
- If someone else wants to reuse your code, what do they need to know?
  - This is important, as Python has no type checking
- Shows info when you hover over code in an IDE
- Can automatically generate a webpage with your documentation

<br>

## Public vs. Private

- **Public** attributes and methods
  - Usable from code outside of the instance
  - "Permanent" public interface
- **Private** attributes and methods
  - Usable within an instance (and possibly instances of a subclass)
  - No direct access from other objects
- **Protected**
  - Usable within a module or by subclasses
  - Kind of between public and private
- Python does not explicitly enforce public/private.
- Convention: start private variables and methods with underscore.
- ***Name mangling***:
  - Start name with double underscore - to be safer
  - But we can still access these using: `obj._ClassName__variableName`
  - *Example*: [name_mangling.py](name_mangling.py)

<br>

## Instance vs. Class vs. Static

### **Instance**

- Methods: take `self` as an argument
- Variable: attached to a particular instance of a class
  - Each instance has separate copies of the variable

### **Class**

- Methods: take `cls` as argument
- Variables: attached to the class instead of an instance
  - Each instance can access the class variable; uses the same copy of the class variable

### **Static**

- Not associated with any class or instance.
- Present in a class just for organizational purposes.
- Not much of a difference between static and class variables.

*Example*:
- [static.py](static.py)
- Java: [MyClass.java](MyClass.java)
- C++: [static.cpp](static.cpp)

<br>

## Confusion with Mutable Defaults

- Careful with mutable objects as defaults.
- It is created once when the `def` statement is run.

```python
class classA:
    def __init__(self, names=[]):
        self.my_names = names
        self.my_names.append("Tim")

obj1 = classA()
obj2 = classA()                 # will append to the same copy of names as obj1
obj3 = classA(["Shelly"])

print(obj1.my_names)            # gives ["Tim", "Tim"]
print(obj3.my_names)            # gives ["Shelly"]
```

### **Mutability in Python**

<center>

| Class    | Immutable? |
| -------- | ---------- |
| `bool`   | Yes        |
| `int`    | Yes        |
| `float`  | Yes        |
| `list`   | Yes        |
| `tuple`  | Yes        |
| `str`    | Yes        |
| `set`    | Yes        |
| `frozenset` | Yes     |
| `dict`   | Yes        |

</center>

### **Solution**

```python
class ClassA:
    def __init__(self, names=None):
        if not names:
            self.my_names = []
        else:
            self.my_names = names
        self.my_names.append("Tim")
```

<br>

## Getters/Setters

- Also called accessors/mutators
- Expose private parts of an object to the public interface
  - `getX()` and `getY()`
  - `setX()` and `setY()`
- Better than using instance variables directly
  - *Why?* We can then check for things like input validity or access permission before setting/getting
- Often a bad idea
  - Why does another object need access?
  - Could the task be achieved within the original object?