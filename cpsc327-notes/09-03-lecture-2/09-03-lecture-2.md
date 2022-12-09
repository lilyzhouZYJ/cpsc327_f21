# 09-03 Lecture 2

## Lecture Today

- More key concepts
- Relationships between objects
- More UML
- Python implementation

<br>

## UML Sequence Diagram

- Top: modules
- y-axis: time
- arrows: method calls

<br>

## Key Concepts

### **Abstraction**
- Removing details that aren't important
- Focus on what is needed

### **Encapsulation**
- Bundling details within a Class; keep them separate from other parts of the program

### **Information Hiding**
- Hiding details that other objects do not care about

### **Public Interface**
- Attributes and methods used to interact with an object from the outside
- Only what is necessary; the rest is hidden
- Need to be very careful when designing or changing this
  - Keep it as small as possible
  - Give clear definitions and documentation

<br>

## Relationships

(listed from weaker to stronger)

### **Dependency**
- One object "uses" another object
- Very broad
- If object A depends on object B and B is changed, then A may need to change
- A common type of *temporary* dependency: taking an object in as a method parameter
  - Temporary because the relationship is only for the method
- UML: dotted line with arrowhead

### **Association**
- More permanent than dependency

### **Aggregation**
- "Has-a" relationship
- Similar to composition, but looser, more general: *Can the object exist on its own?*
- E.g. Object car has passengers, driver, etc.
  - These can exist on their own
- UML: open diamond, on the side of the Object that "has" the other Objects

### **Composition**
- "Has-a" relationship
- Ownership
- E.g. Object car has wheels, engine, etc.
- UML: filled-in diamond, on the side of the Object that "has" the other Objects

### **Inheritance**
- "Is-a" relationship
- E.g. A driver is a person
- More specific version of an object
- UML: open triangular arrowhead

<br>

## Chess Example

- **Object diagram** vs. **Class diagram**
  - Object diagram shows class instances separately
  - Class diagram only shows interactions between classes.

<br>

## Polymorphism

- Objects that share a type (parent class) but can have more specific behaviors

```python
p1 = Queen()    # King and Queen are both Piece objects
p2 = King()

pieces = [p1, p2]

for p in pieces:
    p.move(board)
```

- When we call `move()` on `p1`, it will call the `Queen` move
- When we call `move()` on `p2`, it will call the `King` move

### Python Duck Typing

- "If it walks like a duck and quacks like a duck, then it must be a duck"
- A step further than polymorphism:
  - Doesn't matter if `p` inherits from `Piece`
  - As long as `move` is defined for `p`, it will run
- **EAFP** (easier to ask for forgiveness than permission)
  - As opposed to **LBYL** style (look before you leap)
- *Example*: [duck.py](./duck.py)

<br>

## Creating Classes/Objects

*Example*: [point.py](point.py)