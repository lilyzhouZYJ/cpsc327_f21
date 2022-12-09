# 09-22 Lecture 7

## Lecture Today
- Exceptions and error handling (Chapter 4)
- Logging

<br>

## Error Handling

- Check for exceptional cases
- Why can't we just check for every case?
  - Hard to do this
  - Code becomes clustered
  - Checks have to run every time even if the error is rare
    - Inefficient

<br>

## Exceptions and OOP

- Easier to ask forgiveness than permission (EAFP)
  - When something goes wrong, then we handle it
- Exceptions are objects
  - Declared as classes that inherit `Exception`
  - We may define our own classes of exceptions
- In a `try...except` block, exceptions are matched based on inheritance
  - Want it to match the most specific version first
- Sometimes used for deliberate control flow (not just errors)
- *Example*: [input_check.py](./input_check.py) - demonstrates how to handle errors using i) checks, and ii) exception handling

*Example* - defining our own exception class:
```python
class OutOfStock(Exception):
    pass
```

<br>

## Exception Hierarchy

- All exceptions inherit from `BaseException`
- Three types of exceptions inheriting from `BaseException`
  - `SystemExit` - hitting the X in window corner; `ctrl+D`; `sys.exit(0)`
  - `KeyboardInterrupt` - `ctrl+C`
  - `Exception`
    - Most other exceptions will inherit from `Exception`
- Generally we do not want to catch anything other than `Exception`:
  - Because then we cannot exit the program

<br>

## What Happens when an Exception is Raised?

1. Control flow is interrupted.
2. If inside a `try` block, check `except` clauses to see if they match the exception type.
3. If a match is found and exception handled, the program skips everything in `try-except` and continues after it.
   - If there is a `finally` clause, it will run regardless of whether `try` raises an exception (even if the `try` or `except` blocks had a return statement)
4. Otherwise, go up in scope. The function exits and the calling code is treated as having thrown the exception.
5. Repeat from 2.
6. If exception reaches the top of the stack, program terminates and prints traceback.

```python
# demonstrate finally
def foo():
    n = None
    while n is None:
        try:
            s = input("Please enter an integer:")
            n = int(s)
        except ValueError:
            print("%s is not an integer.", % s)
            return                                          # even though it returns here
        except EOFError:
            pass
        except Exception as err:
            print(err)
        finally:
            print("finished with the try except block")     # the finally clause will still run

# exception travels up the call stack
try:
    foo()
except Exception:                       # if foo fails to handle an exception, it will travel up here
    print("foo had an unhandled exception")
else:                                   # else runs if try clause has no exception
    print("No exception was raised in try")
```

<br>

## Exception Tips

- If a built-in exception type fits, use it
  - More readable and reusable
  - E.g. `ValueError` (right type, wrong value), `TypeError` (wrong type)
- Multiple small `try` blocks may be better than one large `try` with multiple `except`
  - Less likely to handle the wrong exception by accident
  - Remaining code in `try` is skipped when an exception is handled
- Sometimes it is okay to propagate an exception rather than handling it
  - The calling code may know how to handle it better
- Avoid suppressing exceptions (catching and doing nothing)
- Exceptions can be nested
  - Not necessarily bad as long as it remains readable
  - Similar to nested `if/else`

<br>

## Logging

- Valuable for error handling and debugging
- Caught an exception to keep the program running, but still want to know about it
- How can we do better than `print()`?
  - Separate logs from primary output
  - Filter by importance
  - Easily change output stream, format, and log level

### Logging Module

- `import logging` (singleton, global for whole program)
- Levels:
  - Critical
  - Error
  - Warning
  - Info
  - Debug
  - Notset

*Example*: [logging_example.py](./logging_example.py)

```python
import logging

# log messages to a file, ignoring anything less severe than ERROR
logging.basicConfig(filename='myprogram.log', level=logging.ERROR)

# these messages should appear in our file
logging.error("The washing machine is leaking!")logging.critical("The house is on fire!")
# but these ones won't
logging.warning("We're almost out of milk.")
logging.info("It's sunny today.")
logging.debug("I had eggs for breakfast.")

try:
    age = int(input("How old are you? "))
except ValueError as err:    
    logging.exception(err)          # error level
```