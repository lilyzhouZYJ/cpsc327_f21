# 10-01 Lecture 10

## `tkinter` Widget Variables

- Variable objects: `StringVar`, `IntVar`, `DoubleVar`, `BooleanVar`
- Attach to widgets using `variable` or `textvariable` attribute
  - The variables change when the widget changes; and the widget changes when the variables change

<br>

## Object Relational Mapper

- Useful technique in object-oriented languages
- Translate high-level objects into database tables/queries/transactions
- Storage model can be mixed with functioning model
- Python has `SQLAlchemy` and `DjangoORM`
- Instead of manually saving and pickling objects (which is also restricted to Python), let's store them in a database and synchronize it as we use the app

<br>

## SQLite

- Database stored in a single cross-platform file
  - No separate server process
- No configuration or authentication needed
- Good for prototyping or small simple databases
  - Can migrate to a more fully featured database later on if needed
- 5 data types: `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`
- SQL commands
  - `CREATE`, `ALTER`, `DROP`, `INSERT`, `UPDATE`, `DELETE`, `SELECT`

<br>

## Testing (Chapter 12)

We write tests to ensure that...
- The developer understood the requirements
- Code is working the way the developer thinks it should
- Code continues to work when we make changes
  - Regression testing
- The code we are writing has a maintainable interface

<br>

## Types of Testing

### **Black Box Testing**
- Internal structure/design/implementation is unknown
- High-level acceptance testing
- Generally related to input/output
- Real world use cases

### **White Box Testing**
- Internal structure/design/implementation is known
- ***Unit testing***
  - Test the smallest possible pieces independently
  - Good object-oriented code should be easy to unit test
    - Code is already modular
    - Test individual methods
- ***Integration testing***
  - Test the interaction between smaller components
    - Modules and classes working together
    - Database connections
    - Web APIs
  - Often needs a consistent development environment
    - virtualenv
    - Docker

### Who is responsible for each type?

- Software developer: white box testing
- Administrators/managers/PMs: black box testing

<br>

## Test-Driven Development

- Write the tests first
- This establishes how the code will be used
- Then write the implementation
- If the code isn't easy to unit test, then you might rethink the design

<br>

## DevOps and Continuous Integration

- Automate the build/test/deployment processes
- Often integrated with version control
- *Examples*:
  - Travis CI
  - Jenkins
  - Circle CI
  - Github Actions

<br>

## Unittest Framework in Python

- Test class extends `unittest.TestCase`
- Each test is a method in that class with a name starting with `test_`
- Call assertion methods
- Run test from module or use `python -m unittest` to run all tests

*Example test class*:

```python
import unittest

def average(seq):
    return sum(seq) / len(seq)

class TestAverage(unnitest.TestCase):
    def test_zero(self):
        # making sure we get the ZeroDivisionError
        self.assertRaises(ZeroDivisionError, average, [])

    def test_with_zero(self):
        # context manager:
        # if nothing in the context raises ZeroDivisionError,
        # assertRaises will give an error
        with self.assertRaises(ZeroDivisionError):
            average([])

if __name__ == "__main__":
    unittest.main()
```