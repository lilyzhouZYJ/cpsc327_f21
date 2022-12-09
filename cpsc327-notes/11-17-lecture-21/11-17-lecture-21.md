# 11-17 Lecture 21

## Flyweight Pattern

- **Structural** pattern
- Making large numbers of separate objects from a class is very flexible (each can be changed individually)
- This uses lots of space for a lot of identical data
- Flyweight saves memory by keeping shared state in a single object
- **Intrinsic state**:
  - Independent from context
  - Shared in flyweight object
- **Extrinsic state**:
  - Specific context
  - Passed to the flyweight when calling methods

### Class Diagram

- `FlyweightFactory` class:
  - `getFlyweight(repeatingState)`
- `Flyweight` class:
  - Stores `repeatingState` as instance variable
  - `operation(uniqueState)` function
- In the context, we create `Flyweight` using `getFlyweight(repeatingState)`
  - We can then call `Flyweight.operation(uniqueState)` and pass the unique/extrinsic states into the method

### Example 1

- `Game` object with a lot of `Particle`s
- Each `Particle` object has a bunch of parameters:
  - Coordinate
  - Vector
  - Speed
  - Color
  - Sprite
- How do we save memory?
  - We can have a `MovingParticle` that stores the intrinsic states
  - The `Particle` class inherits from `MovingParticle`
  - The `Game` object would now store a single `MovingParticle`, along with the list of `Particle`s

### Example 2

- Images loaded in browser
- Only needs to fetch the image once
- Its position is extrinsic state, but the image data is intrinsic
  - Display the cached image at different positions

### Example 3

- Characters in a word processor
- A character can have a position, font, color, size...
- Should every character be its own object? No!
  - Each character can be a flyweight object and we pass in the necessary context to draw it in the window

### Flyweight Discussion

- Meant for memory *optimization*
- Reminiscent of some data compression algorithms
- Good in certain scenarios, but overkill for others
- Increases complexity
- Specific context is managed by the clients which could be easy or hard depending on the application

<br>

## Memento Pattern

- **Behavioral** pattern
- Save the state of an object in a snapshot
  - Downside: the storing action consumes memory
- Can restore a previous state from a snapshot (undo)
- Avoids exposing the details of the original class
  - Have the original object create Mementos and then pass these to Caretaker, to avoid exposing the information in the original object
- Lifetime of snapshots should be managed by caretaker code
- Can be used alongside the *command* pattern

### Class Diagram

- `Originator` class:
  - Has some `state`
  - `save()` returns `Memento` object
  - `restore()`
- `Memento` class:
  - Saves the `state`
  - Constructor: `Memento(state)`
- `Caretaker` class
  - `Originator` instance
  - `history`: a list of `Memento` objects
  - `undo()` function restores to previous state based on `history`

### Example

- `Editor` class:
  - States;
    - `text`
    - `cursorPos`
    - `selection`
    - `currentFont`
    - `styles`
  - `makeSnapshot()`: returns `Snapshot` object
  - `restore(Memento)`

<br>

## Concurrent Programming

- **Process**
  - Everything needed to run
  - Process ID
  - Virtual address space
  - Code
  - Handles to open files (and other resources)
  - Security context
  - Environment variables
  - At least one main thread
- **Thread**
  - Scheduled for execution on a core of the CPU (by the OS)
  - Shared virtual address space
    - With other threads in the same process
  - EVery thread has independent execution context:
    - Program counter
    - Machine registers
    - Stack