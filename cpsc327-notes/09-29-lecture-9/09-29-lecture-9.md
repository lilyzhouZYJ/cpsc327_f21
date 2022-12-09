# 09-29 Lecture 9

## Topics Today

- Callback functions
- Event-driven GUI framework
- Database ORM

<br>

## Functions as Objects

- Functions can be passed around, modified, called later, partially applied
- Any object can act like a function by making it callable
- Monkey patching
- *Example*: [event_timer.py](./event_timer.py)

<br>

## First-Order Functions in Event-Driven Frameworks

- **Event-driven programming**:
  - Flow of the program comes from user interaction (or other forms of input)
- Almost all GUI's are event-driven
- One main loop
- Listens for events
- Triggers **callback functions**
- OOP is a nice complement when building with a Widget toolkit
  - **Widgets** - with callback functions attached to them

<br>

### `tkinter` Framework

- `tkinter` is the main built-in widget toolkit in Python
- OOP interface
- Attach callback functions to widget objects representing elements ina window
- Widget objects can stay put, move around, be deleted
- Drawing each frame is abstracted away
- *Example*:
  - See `gui.py`
  - Building on `Notebook` without changing existing code (See `notebook_gui` directory)

### Widget Variables

- StringVar, IntVar, DoubleVar, BooleanVar
- Attach to widgets using `variable` or `textvariable` attribute