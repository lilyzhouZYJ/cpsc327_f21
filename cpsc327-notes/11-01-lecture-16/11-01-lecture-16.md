# 11-01 Lecture 16

## Iterators

- **Behavioral** pattern
- An iterator object is created to traverse elements from another object
- Iterators are a common object-oriented pattern
- Classic: `for` loop
  - Iteration is controlled externally using index `i`
- General iterator pattern:
  - Iteration controlled internally
  - `while not iterator.done(): print(iterator.next())`

```py
class Iterator:
    def prev():
        #
    def current():
        #
    def set_current(e):
        #

for x in Iterator:
    #
```

- This pattern is baked into many languages
  - Python: all `for` loops use iterators
  - Java: `for each` loops when an object implements `Iterable` interface
    - `for(Element x : elementList)`
  - C++: incrementing/decrementing pointers steps through arrays (size aware)and classes can overload pointer operations

### **Iterator Protocol**

- An object that is "iterable" must implement `__iter__`, which returns an `Iterator` object
- The iterator must implement `__next__` and when it is done it must raise a `StopIteration` exception

```py
lst = [1,2,3]
lst_iter = lst.__iter__()
lst_iter2 = lst.__iter__()      # same as iter(lst)

next(lst_iter)
next(lst_iter)
next(lst_iter2)
# the two iterators will be in different places; do not influence each other
```

### **Iterators in Python**

- `for` loops only work on iterators
  - `for(i, x) in enumerate(lst):`
    - `i` is index, `x` is element
- Also used for **comprehensions** and **generators**
- *Examples*: 
  - [capital_iterator.py](./iterator/capital_iterator.py)
  - [LinkedList.py](./iterator/LinkedList.py)
- Could also use **`yield`**:
  - `yield` causes a function to return a Generator object
  - Will continue executing after `yield` when `next()` is called on the Generator object
  - *Examples*:
    - [LinkedList_yield.py](./iterator/LinkedList_yield.py)
    - [filesystem_walk.py](./iterator/filesystem_walk.py)

### **Yield From Another Iterable**

- `yield from` fetches data from another generator

```py
# original:
def read(g):
  for item in g:
    yield item
  
# with yield from
def read(g):
  yield from g
```

*Examples:*

```py
# passing filename instead of sequence
def warnings_filter(filename):
  with open(filename) as file:
    yield from (l.replace("WARNING", "") for l in file if "WARNING" in l)

filter = warnings_filter(filename)
for l in filter:
  print(l)
```

```py
# walking through a file system
# see filesystem_walk.py
def walk(file):
  if isinstance(file, Folder):
    yield file.name + "/"
    for f in file.children:
      yield from walk(f)
    else
      yield file.name

for x in walk(root):
    print(x)
```

### **Comprehensions**

- Allow us to transform or filter an iterable object in as little as one line of code
- List comprehensions:
  - `output = [int(num) for num in input_strings]`
    - `int(num)` will be applied to every item of `input_strings` list
  - `output = [int(num) for num in input_strings if len(num < 3)]`
    - `int(num)` will be applied to all items of `input_strings` that have lengths less than 3
- Set and dictionary comprehensions:
  - `books = {b.author for b in books if b.genre == "fantasy"}` - set
  - `books = {b.title: b for b in books if b.genre == "fantasy"}` - dictionary

### **Generators**

- If we are just looping over items one at a time and do not need to have a complete container (e.g. list or dictionary), then creating that container wastes memory
- Solution: we can use generator expressions, which ***do not create a final container object***

```py
# remove all lines with WARNING in it
with open(fileName) as file:
  warnings = (log for log in file if 'WARNING' in log)  # warnings is generator obj
  for w in warnings:
    print(w.replace("WARNING", "")); 
```

**Above program, but with object oriented programming:**

```py
class WarningFilter:
  def __init__(self, inSequence):
    self.inSequence = inSequence
  
  def __iter__(self):
    return self
  
  def __next__(self):
    line = self.inSequence.readline()
    while line and "WARNING" not in line:
      line = self.inSequence.readline()
    if not line:
      raise StopIteration
    return line.replace("WARNING", "")
  
with open(fileName) as file:
  filter = WarningFilter(infile)
  for w in filter:
    print(w)
```

**Above program, but with generators:**

```py
# yield causes warnings_filter to return a generator object
def warnings_filter(inSequence):
  for l in inSequence:
    if "WARNING" in l:
      yield l.replace("WARNING", "")

with open(fileName) as file:
  filter = warnings_filter(file)  # filter is a generator object
  for w in filter:
    print(w)
```

- `yield` is like `return`, but unlike `return`, when the function is called again (via `next()`), it will start where it left off--on the line after the `yield` statement
- `warnings_filter()` actually ***creates a generator object***, with `__iter__` and `__next__` method on it

<br>

## Decorator Pattern

- **Structural** pattern
- Add capabilities to an object dynamically (without monkey patching)
  - *Wrap* an object with core functionality with another object that alters this functionality
- Can recursively wrap with more decorators
- Core interface remains untouched
  - The interface of the decorated object remains identical to that of the core object
- Another pattern that made its way into Python syntax

### Inheritance vs. "Composition"

- Note that "composition" is sometimes used as a catch-all term for "has-a" relationship
- Inheritance is static, where as composition "has-a" relationships are more flexible by swapping out a reference
  - Inheritance is kind of like composition if you think about the subclass as holding a reference to the parent. But this reference cannot be changed, and you only get one (unless willing to deal with multiple inheritance)

### Class Decoration

- Using inheritance:
  - *Example*: [decorator.py](decorator/decorator.py)
- Static decoration using `@Decorator` annotation
  - *Example*: [class_decorator_annotations.py](decorator/class_decorator_annotations.py)

### Function Decoration

- We can also **decorate functions**
  - Remember that functions are objects
- Special syntax for statically defined decorators
  - `@decorator_name` before definition
  - Less powerful
    - Baked into the source code
    - Cannot do it at runtime
  - Often easier to read
- *Example*: [log_calls_decorator.py](decorator/log_calls_decorator.py)