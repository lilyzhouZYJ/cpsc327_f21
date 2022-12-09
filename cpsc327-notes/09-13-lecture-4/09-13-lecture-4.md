# 09-13 Lecture 4

## Review: Getters/Setters

- Also called accessors/mutators
- Expose private parts of an object to the public interface
  - `getX()` and `getY()`
  - `setX()` and `setY()`
- Better than using instance variables directly
  - *Why?* We can then check for things like input validity or access permission before setting/getting
- Often a bad idea
  - Why does another object need access?
  - Could the task be achieved within the original object?

<br>

## Python "Properties"

- Convenience of dot notation access
- Benefits of method access
- Still should only use getters/setters when needed

```python
# syntax
property(getter, setter, deleter, docstring)

# example
class Color:
  def __init__(self, rgb_value, name):
    self.rgb_value = rgb_value
    self._name = name
  
  def _set_name(self, name):
    if not name:
      raise Exception("Invalid Name")
    self._name = name
  
  def _get_name(self):
    return self._name

  # make name into property:
  # set getter (_get_name) and setter (_set_name)
  name = property(_get_name, _set_name)

# now we can just use Color.name
Color.name = "new name"       # use the setter
print(Color.name)             # use the getter
```

<br>

## Notebook Case Study

- [textbook_notebook](./textbook_notebook)
- [our_notebook](./our_notebook)

Note the composition relationship between Note and Notebook.

<br>

## Using/Overriding Parent Class

- `super()` or `super(CurrentClass, self)`
  - Accesses the functionality of the parent class
  - Often needed in `__init__`, but may also be used elsewhere
  - May appear anywhere in a method
  - Most specifically useful when taking something from the parent and modifying it
- If you are adding parameters, then we could do this:

```python
def __init__(self, new_parameter, *args, **kwargs):
    self.foo = new_parameter
    super().__init__(*args, **kwargs) # we don't care about what the params are
```

<br>

## `*args` and `**kwargs`

- ***Packing*** arguments into tuple or dict
  - `def foo(*args, **kwargs)`
  - Normal args come before keyword args, so `*args` precedes `**kwargs`
- ***Unpacking*** a list
  - `a = [1,2,3]`
  - `foo(*a)` => unpacks the list into arguments for the function `foo`
- Packing the arguments
  - `def foo(a = None, b = None)`
  - using `for x in *args`in `foo` => packs the arguments of the function `foo` into a list
- Unpacking a dict
  - `a = {"a":1, "b":2}`
  - `foo(**a)` => unpacks the dict into keyword arguments for function `foo`
    - The same as `foo(a = 1, b = 2)`
