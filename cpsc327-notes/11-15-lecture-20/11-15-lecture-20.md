# 11-15 Lecture 20

## Remaining Patterns

- Command
- Abstract factory
- Flyweight
- Composite
- Memento
- ...

<br>

## Command Pattern

- **Behavioral** pattern
- Represent an action as an object
- Object-oriented callback
- Useful for deferring execution
- Easier to add or extend actions available
- Can help with undo/redo since the action can have a method to reverse itself

### Example

- Instead of having multiple user interfaces call a `save()` function, we can add a `Save` command which all the interfaces call. This way we can extend/modify the command without having to update every user interface.
- Examples:
  - [window_command.py](./command/window_command.py)
  - [pythonic_window_command.py](./command/pythonic_window_command.py)
    - Using functions and `__call__()` instead of Command objects

<br>

## Abstract Factory and Factory Method

- **Creational** pattern
- Create related objects without specifying the concrete classes
- The abstract factory determines which concrete type to create, based on some input, configuration, or platform specific information
- Factory methods that are like constructors, but may re-use objects, create objects of a subclass, have more descriptive names for what they create

### Factory Method Class Diagram

```py
Product p = createProduct()
p.doStuff()
```

- `Creator` class:
  - Dictates that `createProduct()` must be defined, which creates a `Product` instance
  - Has to decide which concrete creator to call
- `ConcreteCreatorA` class:
  - Has `createProduct()` which creates a `ConcreteProductA` instance
- `ConcreteCreatorB` class:
  - Has `createProduct()` which creates a `ConcreteProductB` instance
- `Product` interface:
  - Dictates that `doStuff()` must be defined
- `ConcreteProductA`: has `doStuff()`
- `ConcreteProductB`: has `doStuff()`

### Abstract Factory Class Diagram

- `Client` class:
  - Instance variable points to an `AbstractFactory` object
- `AbstractFactory` interface:
  - Has to determine which concrete factory to create
- `ConcreteFactoryA` class
- `ConcreteFactoryB` class

### Examples

- [abstractfactor.py](./abstract-factory/abstractfactory.py)
- Region-specific formatting: [formatter_factory.py](./abstract-factory/formatter_factory.py)

<br>

## Composite Pattern

- **Structural** pattern
- Building trees through object references
  - Also potentially linked lists and graphs (anything node/pointer based)
- Polymorphism allows individual objects (leaves) and collection objects (internal nodes) to be treated as one type
  - More important for statically typed language

### Class Diagram

- `Component` class: root of the tree
  - `doThis()` function
- `Leaf` child class: extends `Component`
  - `doThis()`
- `Composite` child class: extends `Component`
  - `elements`: list of child nodes
  - `addElement()`
  - `doThis()`

*Note its similarity with Decorator class diagram.*

### Examples

- [folder_composite.py](./composite/folder_composite.py)