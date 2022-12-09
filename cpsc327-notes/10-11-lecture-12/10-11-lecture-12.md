# 10-11 Lecture 12

## How much testing do we need?

- Have we tested enough cases?
  - Checking **boundary conditions**
  - Hard to quantify
- How much of the code was tested?
  - **Code coverage**
  - Easier to quantify
- Could we automate the generation of tests?
  - **Symbolic execution**
  - **Fuzzing**

<br>

## Boundary Values

- Values at the boundary of conditions
- For example, a function that converts a numeric grade to A, B, C, D, F
  - 89 and 90 are boundary values
  - 81-88 are less important to check
- We should focus testing on these boundaries

<br>

## Control Flow Graph

See slides.

<br>

## Code Coverage

- **Function coverage**
  - Has each function in the program been called?
- **Statement coverage**
  - Has every statement in the program been executed?
- **Branch coverage**
  - Has each branch of each control structure been executed?
- **Edge coverage**
  - Has every edge in the control flow graph been executed?
  - *Very similar to branch coverage*
- **Condition coverage**
  - Has each Boolean sub-expression evaluated both to true and false?

### Using `coverage` Module

- `coverage run -m pytest`
- `coverage report` => generate report, after running the program
- `coverage html` => generate website report

*Example config file*:

```python
# .coveragerc to control coverage.py
[run]
branch = True   # by default branch coverage is not counted
source = ./
omit = tests/*
```

<br>

## Symbolic Execution

- Analyze the code to determine what inputs lead to different paths in the CFG
- Find constraints on inputs that could possibly lead to bugs
- Difficulties with memory aliasing and path explosion
  - *Memory aliasing*: multiple ways of getting to the same value
  - *Path explosion*: the number of paths grow as the program grows

*Example*:

```python
int foo() {
    ...
    y = read();
    z = y * 2;
    if (z == 12) {
        fail();
    } else {
        printf("OK);
    }
}
```

- We can read through the code to recognize that `y == 6` and `y != 6` would trigger the two conditional statements, respectively. We can then perform testing using values such as `y = 6` and `y = 5`.

<br>

## Fuzzing

- Very popular security research area in recent years
- Essentially large-scale randomized input testing
- Instead of worrying about finding the right boundary values, you could just try everything!
- Ideally inputs have some structure so that we don't waste time with rejected inputs
  - Could be randomly mutated from a set of normal inputs
  - Could have a grammar or protocol
- Chrome is continually being fuzzed

<br>

## Example of Patching

```python
@pytest.fixture()
def savings_account():
  return SavingsAccount()

def test_add_transaction(savings_account):
  t1 = Transaction(500)
  savings_account.add_transaction(t1)
  assert len(savings_account._transactions) == 1

  with patch.object(savings_account, "_check_balance") as x:
    with patch.object(savings_account, "_check_limits") as y:
      # mock the behavior of these accounts
      x.return_value = False
      y.return_value = True
      print(savings_account._check_balance(t1))
      savings_account.add_transaction(Transaction(10))
  assert len(savings_account._transactions) == 1
```