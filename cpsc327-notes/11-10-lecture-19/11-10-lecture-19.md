# 11-10 Lecture 19

## State Machine: Example

- [xml_state_parser.py]
  - Problem: creating new `ChildNode` objects repeatedly which need to be garbage collected when the state changes => solution: **singleton** design pattern

## Miscellaneous

- [Java Design Patterns](https://java-design-patterns.com/)

<br>

## Singleton Pattern

- **Creational** pattern
- Make sure a class only ever has one instance
- Lazy initialization
  - Don't create the instance until something has to use it
- Need global access
  - Typical for all class definitions
  - Instances are typically not global; we can make them global by accessing them through the class

### Class Diagram

- `Singleton` class:
  - contains a `Singleton` object as instance variable
  - `Singleton()`
    - Need to make sure no `Singleton` object has already been created
  - `getInstance(): Singleton`
    - Returns the instance of `Singleton` object

### Example

- President of the USA object
  - The president can change
  - But only one president at a time

### Problems

- Very situational
- Should always be careful making anything global
- Troublesome for concurrent code
  - Accessing the global singleton could cause conflicts; synchronization issue
- Maybe the code should be extended to allow multiple instances someday
- In most cases you can pass around an object in method parameters instead of making it global

### Use Cases

- Logging objects
  - One global logger to manage all log messages
- Application configuration objects
  - Global configuration for the project
- Objects with no internal state as in the Strategy and State patterns
- Objects with read-only state
- Some other design patterns can use it

### Singleton in XML Parsing Example

- [xml_singleton_state_parser.py]:
  - Creating a module-level instance for each of `FirstTag`, `ChildNode`, etc., to serve as singletons
  - But there is nothing prohibiting the code from creating more instances somewhere

- [xml_state_parser.py]
  - `XmlState` abstract class:
    - Class variable: `_instance` initialized to None
    - `__new__(cls, *args, **kwargs)` class method: (first thing that is called ???)
      - Checks if `cls._instance` exists
      - If not, create an ???
    - `get_instance(cls, *args, **kwargs)` class method:
      - Checks if `cls._instance` exists
      - If not, create by `cls._instance = cls(*args, **kwargs)`
  - The `XmlState` class is inherited by classes likes `ChildNode`, `FirstTag`, etc.

<br>

## Template Method Pattern

- **Behavioral** pattern
- For factoring out duplicate code
- Re-used code is defined and called in base class
- Subclasses override only certain steps in a process
- A generalization of the *Strategy* pattern
  - A process with multiple steps instead of a single method

### Class Diagram

- `AbstractClass`:
  - `templateMethod()`: calls `step1()`, `step2()`, and `step3()` in order
  - `step1()`
  - `step2()`
  - `step3()`
- `ConcreteClass`:
  - Inherits `AbstractClass`
  - Can override some step methods

### Example

- Sorting: in descending vs. ascending
- `SortAlgorithm` class:
  - Has a `compare()` method, which can be overriden by subclasses to change descending vs. ascending

