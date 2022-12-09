# 12-01 Lecture 23

## Refactoring

- Like editing a book before publication
- Goal: improve your code to make it "cleaner"
  - Easy to read
  - Minimal redundancy
  - Modular
- Sometimes this means taking advantage of design patterns
- Very helpful to have tests in place to avoid breaking things
  - Some tests may need to be refactored too
- Paying off "technical debt"

<br>

## When to Refactor

- Rule of three: refactor when you write something similar three times
- When adding a new feature
- When fixing a bug
- During code review

<br>

## Code Smells

- Signs of problematic code
  - Varying in degrees
- Incur long term technical debt
- Primary targets when refactoring
- [refactoring.guru](https://refactoring.guru/) is a great source
  - For each code smell they give multiple options to address the issue

### Bloaters

- **Long method/large class** - *code that tries to do too much*
  - Extract into multiple methods/classes
- **Primitive obsession** - *using primitive datatypes too much is inflexible to future changes*
  - Replace with small objects
- **Long parameter list** - *too many arguments make calls hard to read*
  - Pass in objects/structs that group related data
  - Could also store some data in instance variables

### OOP Abuse

- **`switch` statements** (or long `elif` chains in Python)
  - Use polymorphic objects instead
- **Temporary instance variables** - *instance variables that are not always needed*
  - Group these into their own classes
  - Instead of checking if the object exists, introduce null object that has default behavior
- **Refused bequest** - *lots of unused code from parent class*
  - Hierarchical relationship might not be appropriate
  - Replace with composition
- **Alternative classes with different interfaces**
  - Identify the common denominator
  - Deduplicate the code

### Change Preventers

- **Divergent change/shotgun surgery**
  - Often due to copy/pasting code
  - Making a change to one method forces you to adjust many other methods
- **Parallel inheritance hierarchies**
  - You subclass one class and find that it needs a corresponding subclass for another
  - Move required functionality into one hierarchy

### Dispensables

- **Comments**
  - Too many/too long
  - Code is incomprehensible without them
  - Good class/method names can make OOP code self-documenting
- **Duplicate code**
- **Lazy class**
  - Doesn't do enough to justify the added complexity
- **Data class**
  - If a class only holds data
- **Dead code**
  - Variable, parameter, method, or class no longer used
- **Speculative generality**
  - Unused code created prematurely

### Couplers

- **Feature envy**
  - Method uses data from another object more than its own
  - Move to the other class
- **Inappropriate intimacy**
  - A method needs private data from another class
  - Move method or delegate to another method
- **Message chains**
  - `obj.method1().method2().method3()`
  - Delegate to a single method
- **Middle man**
  - A class does nothing other than delegate

