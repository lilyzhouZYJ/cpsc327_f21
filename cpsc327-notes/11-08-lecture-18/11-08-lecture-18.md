# 11-08 Lecture 18

## Observer Pattern

- **Behavioral** pattern
- Observers are "subscribed" to updates on one or more other objects
- An object can have multiple observers
  - Either composition or aggregation
- Observer object can be added or removed at runtime
- Used in event-driven programming
  - Event queue is the subject
  - Handlers are observers
- The "view" part of Model-View-Controller
  - GUIs and websites

### Design

- The subject does not need to know what the observer does; it just notifies the observer
- The subject does not "push" the data needed to the observer
  - i.e. no argument to `update()`
- Instead, the observer "pulls" what data it needs
  - Relevant data would have to be publicly accessible
- Pushing is also possible, but has drawbacks
  - `update(data)`
  - What data to send?
    - Different observers may need different data
    - Send everything? - might as well just make it public
      - Also violates encapsulation principle
  - Need to know what the observer does, which is bad for abstraction
- Other considerations:
  - If a lot of small changes are made, should the subject upadte after a batch?
    - Depends on the design
  - Can an observer watch multiple subjects?
    - `update` needs to indicate which subject changed
    - What challenge does this create for memory management?
      - Problem with garbage collection: subject may not be able to delete an observer, for it could still be referenced by other subjects

### Example

- Auction:
  - The bidders need to be notified when a new highest bid has been added
  - The bidders are observers in this case

### Observer Class Diagram

- `ObserverInterface`: `update()`
- Observer classes: `Observer1`, `Observer2`
  - Extends or inherits `ObserverInterface`
- Core subject: `Core`
  - `attach(Observer)`
  - `setState()`
  - `getState()` 

<br>

## Strategy Pattern

- **Behavioral** pattern
- Implement different solutions to a problem, each in a different object
- Choose the appropriate solution at ***runtime***
- Strategy objects have only one function and no data
- Can be simplified a bit by using first-class functions
- This is essentially still the strategy pattern since functions are objects

### Class Diagram

- `Client`
- `Context`: determines which exact strategy/implementation to use
  - Could be merged as a part of `Client` class
- `Strategy`: `someAction()` - abstract function
- `ConcreteStrategy1`: `someAction()` - inherits `Strategy`
- `ConcreteStrategy2`: `someAction()` - inherits `Strategy`
- We can have the client call the correct `someAction()` by swapping out the strategy stored in `Context`

<br>

## State Pattern

- **Behavioral** pattern
- Similar to strategy pattern
- For problems that make sense as state machines
- Behavior of an object changes based on its state
- Transitions may be defined in manager or in state classes themselves

### Class Diagram

- `User`
- `Context`: `current_state`
- `State`: `process(context)` - abstract
- `State1`: `process(context)` - inherit `State`
- `State2`: `process(context)` - inherit `State`
- `State3`: `process(context)` - inherit `State`

Compare to Strategy pattern: not just swapping states, but also need state transitions.

### Example

- XML parsing
