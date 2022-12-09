# 10-06 Lecture 11

## Unittest Framework

- Test class extends `unittest.TestCase`
- Each test is a method in that class with a name starting with `test_`
- Call assertion methods, from `unittest.TestCase`
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

### **Organizing Tests**

- Group tests into classes based on shared `setUp`/`tearDown`
```
ourprog/
    ourprog/
        __init__.py
        db.py
        gui.py
        rules.py
        test/
            __init__.py
            test_db.py
            test_gui.py
            test_rules.py
    set_up.py
```

### **`setUp` and `tearDown` Methods**

- `setUp` method
  - Run authomatically before each test
  - Create necessary objects or data
- `tearDown` method
  - Run automatically after each test
  - Clean up anything that isn't simply replaced or garbage collected
  - E.g. test that reads/writes files, like logs or database writes

### **`setUpClass` and `tearDownClass` Methods**

- class methods that run once before all the tests and once after all the tests

```python
class TestValidInputs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
```

### **Skipping Tests**

- Code being tested is not yet implemented
- The test depends on the OS you are using
- Label these tests so they don't distract from the ones we care about
  - `expectedFailure()`
  - `skip(reason)`
  - `skiplf(condition, reason)`
  - `skipUnless(condition, reason)`

*Examples*:
- [test_stats.py](./test_stats.py): illustrates testing
- [test_skipping.py](./test_skipping.py): illustrates skipping tests

<br>

## Pytest Framework

- Another popular testing framework
- Compatible with `unittest`
- More detailed output
- Does not require object-oriented tests
- Runs any functions named `test_*`
- Not built-in for Python
- Run with `pytest test_pytest_stats.py`

*Examples*:
- [test_pytest_stats.py](./pytest/test_pytest_stats.py): simple tests, with fixture
- [test_pytest_setups.py](./pytest/test_pytest_setups.py): illustrates setUps and tearDowns
- [test_pytest_skipping.py](./pytest/test_pytest_skipping.py)
- [test_pytest_cleanup.py](./pytest/test_pytest_cleanup.py)

### **Setup**

```python
@pytest.fixture                     # fixture: methods for setup
def valid_stats():
    return StatsList([1,2,3,4])

def test_mean(valid_stats):
    # valid_stats below will take the return value of the fixture valid_stats()
    # method above and pass it as argument into mean()
    assert valid_stats.mean() == 2.5


# run once before and after all test classes in this module
def setup_module(module)
def teardown_module(module)

# run once before and after all tests of the test class
def setup_class(cls)
def teardown_class(cls)

# run before and after every test
def setup_method(self, method)
def teardown_method(self, method)
```

### **Skipping**

```python
def test_simple_skip():
    if sys.platform != "fakeos":
        pytest.skip("Test works only on fakeOS")

@pytest.mark.skipif("sys.version_info <=(3,0)")     # skip based on version info
def test_python3():
    pass

# expects failure
def test_fails():
    pytest.xfail()
    assert True == False
```

<br>

## Unit Test Mocking

- Monkey patching lets us change methods at runtime
  - Unit testing is probably the most common use case
- Fake the behavior of some code to make tests simpler and more independent
  - Interacting with a database
  - Fetching a file from the internet
  - Faking user input
  - Using fixed timestamps
  - Replacing randomness with consistent data