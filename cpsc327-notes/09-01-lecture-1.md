# 09-01 Lecture 1

## Course Topics

- Object-oriented principles and design
- Implementation in Python
- Exceptions and error handling
- Database ORMs
- Event-driven programming and GUI toolkits
- OOP strengths and weaknesses
- Some advanced features of Python
- Testing
- C++ (language comparison)
- Design patterns
- Refactoring and code smells

<br>

## What is OOP?

- A programming paradigm
- Software is built as a collection of objects that interact with each other
- Other paradignms:
  - **Procedural** (C)
  - **Functional** (Racket)
  - **Logic** (Prolog)
- Another way of breaking down the paradigms:
  - **Imperative**:
    - OOP
    - Procedural
  - **Declarative**:
    - Functional
    - Logic

<br>

## Why OOP?

- Approachable design technique
- Flexibility
- Modularity
- Abstraction
- Code-reuse
- A useful tool for many projects
- Popular in industry with a lot of turnover
- *Not always the best solution!*

<br>

## Object

- What is an object?
  - A bundle of **data** and **behavior**
  - Treat these two as a single unit
- *Example*: Person object
  - Data: name, age, height, address, phone number
  - Behavior: walk, run, eat, sleep, talk
  - Alice and Bob are **instances** of the **class** of Person

<br>

## Object Relationships

- **Unified Modeling Language (UML)**
  - Well-defined language
  - Frequently used informally
  - Useful for object relationships
- **Association** - relationships between objects

<br>

## Object-Oriented Design/Modeling

- Breaking a problem into pieces
- What are the objects involved and how do they interact?

### Example: Elevator

- Is it a system to control the elevator?
- A simulation to test different designs for a skyscraper?
- How does this change the objects involved?
  - Only need to model the relevant objects