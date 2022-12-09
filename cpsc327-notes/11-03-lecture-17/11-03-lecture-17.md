# 11-03 Lecture 17

## Adapter Pattern

- **Structural** pattern
- Convert an interface into another interface
- Allows existing objects to work together without modifying their *rigid* public interfaces
- Also called a **wrapper**
  - Kind of an overloaded term
  - A decorator is also a wrapper, but it doesn't change the interface

### Class Diagram

- *Class adapters* use multiple inheritance
  - Adapter class inherits both TargetClass and AdapteeClass
- *Object adapters* use an object reference to delegate (composition)
  - Adapter class inherits TargetClass and holds reference to AdapteeClass
  - *Examples*:
    - [adapter.py](./adapter/adapter.py)
    - [age_calculator_adapter.py](./adapter/age_calculator_adapter.py)

### Potential Translations in Adapter

- Convert arguments to a different format
- Rearrange the order of arguments
- Call a differently named method
- Supplying default arguments
- *No new behavior!*
  - As opposed to Decorators

<br>

## Facade Pattern

- **Structural** pattern
- Provides a simpler or higher-level interface to some complicated code
- A type of **wrapper** like adapter and decorator
  - No new functionality

### Facade in Python

- So commonly used that it's not always referred to by name
  - `for` loops are a facade over iterators
  - `defaultdict` is a facade over `dict`s to reduce reoccurring code when keys do not exist
  - `requests` library is a facade over lower-level HTTP libraries
    - HTTP libraries are a facade over managing text-based messages over sockets

*Examples*:
- [facade.py](./facade/facade.py)
- [email_facade.py](./facade/email_facade.py)
- [FacilitiesFacade.cpp](./facade/FacilitiesFacade.cpp)