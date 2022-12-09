# 10-25 Lecture 14

## Lecture Today

- C++ crash course
- Upcoming: design patterns

<br>

## Language Comparison

| C++ | Python |
| --- | ------ |
| 35 years old | 29 years old |
| Regular releases (C++21) | Regular releases (Python 3.10) |
| Compiles to platform specific binary code | Program runs as input to python process |
| Manual memory management | Garbage collection |
| | No `public`/`private` |
| Static types | Duck types |
| Enforces `const` | No constants |
| Better for high performance or constrained resources | Better for rapid development |

<br>

## Pointers vs. Reference

- References are new to C++
- Reference is like a `const` pointer
  - Pointer: `int a = 2; int *p = &a;` => `p` is a pointer
  - Reference: `int & p = a;` => `p` is a reference; changing `p` will change value of `a`
- Creates an alias for an existing value
- Unlike a pointer, it does not need to be dereferenced to use the value
- Variables in Python can be thought of as somewhere in between a pointer and a reference
  - `a = "Hello"`
  - `b = "world"`
  - `b = a` => b now points to "Hello", but we don't get the same amount of control as we do with C++ pointers

<br>

## Structs

- Contiguous chunk of memory
- Fields of different types (unlike array)
- A field can be a function
- All fields are publicly accessible
- Accessed with dot `.`

```cpp
struct product {
    int weight;
    double price;
    double calcCost() {
        return weight * price;
    }
};
```

<br>

## Classes

- Functionally nearly identical to struct
  - Default visibility of a class is *private*, whereas default visibility of struct is *public*
- Generally use structs for grouping data only

```cpp
#include <iostream>
using namespace std;

class Rectangle {
    int width, height;    // default: private
public:
    void set_values(int, int);
    int area() { return width * height; }
}

void Rectangle::set_values(int x, int y) {
    width = x;
    height = y;
}

int main(){
    Rectangle rect;
    rect.set_values(3,4);
    cout << "area: " << rect.area();
    return 0;
}
```

<br>

## Visibility

- **Private**
  - Default for classes
  - Only accessible from objects of this class
- **Protected**
  - Accessible to subclasses
    - Different from Python, in which everything in parent class is inherited in subclasses
  - Accessible to friends (other functions that are granted permission)
- **Public**
  - Accessible to anyone

<br>

## Instantiating Objects

- `Person tim;` => allocating space on the stack
- `Person tim ("Tim");` => allocating space on the stack
- `Person * tim = new Person("Tim");` => allocates space on the heap
  - Basically the same as `Person * tim = (Person *) malloc(sizeof(Person));`, except this does not call the constructor

*Compare to Python*:
- In Python, all objects are created on the heap
  - The stack only stores variable references to those objects

<br>

## `new` and `delete`

- Higher level version of `malloc`/`free`
- New dynamically allocates memory on the heap
- Returns a pointer to the object
- Needs to be paired with `delete` to reclaim that memory

```cpp
Person* tim = new Person("Tim");
delete tim;

int* foo;
foo = new int[5];   // new array
delete[] foo;
```

<br>

## Constructor/Initializer

- Function with no return type and name matching the class name
- Can overload constructor with different parameters
- Can initialize in constructor body or initializer list
  - This is better specifically for initializing attributes that are other objects

**Using constructor body**:

```cpp
class Rectangle {
    int width, height;
public:
    Rectangle (int, int);
    int area() { return (width * height); }
};

Rectangle::Rectangle(int a, int b) {
    width = a;
    height = b;
}

int main() {
    Rectangle rect (3,4);
    Rectangle rectb (5,6);
    cout << "rect area: " << rect.area() << endl;
    return 0;
}
```

**Using initializer list**:

```cpp
class Circle {
    double radius;
public:
    Circle(double r) : radius(r) { }                    // initializer list
    /* Circle(double r) { radius = r; }             => alternative */
    double area() { return radius * radius * 3.14; }
};

class Cylinder {
    Circle base;
    double height;
public:
    Cylinder(double r, double h) : base(r), height(h) { }
    /* Alternative: but undesirable for it calls Circle() twice
    - Once with Circle(r)
    - A second time with the = operator, which calls copy constructor
    Cylinder(double r, double h) { base = Circle(r); height = h; }
    */
    double volume() { return base.area() * height; }
}
```

<br>

## `this`

- A pointer to the current instance within a method call
- Similar to `self` in Python
- Not required to access instance variables/methods

```cpp
class Dummy {
public:
    int x;
    bool isitme(Dummy& param);
    Dummy(int x) {
      this->x = x;          // note the use of dereferencing with `this`!!
    }
};

bool Dummy::isitme(Dummy& param){
    if(&param == this) return true;
    else return false;
}

int main(){
    Dummy a;
    Dummy* b = &a;
    if(b->isitme(a))
        cout << "yes, &a is b\n";
    return 0;
}
```

<br>

## Pointers to Objects

- When using a pointer to an object, we need to dereference to access instance variables/methods

| expresion | can be read as |
| --------- | -------------- |
| `*x` | pointed to by x |
| `&x` | address of x |
| `x.y` | member y of object x |
| `x->y` | member y of object pointed to by x |
| `(*x).y` | member y of object pointed to by x (equivalent to previous one) |
| `x[0]` | first object pointed to by x |
| `x[1]` | second object pointed to by x |
| `x[n]` | (n+1)th object pointed to by x |

<br>

## Overloading Operators

- Python and C++ are similar in this way
- Your classes can redefine operators like `+`, `-`, `*`
- `operator<<` is kind of like `__str__`
- `operator==` is like `__eq__`

*Overloadable operators*: `+`, `-`, `*`, `/`, `=`, `<`, `>`, `+=`, `-=`, `*=`, `/=`, `<<`, `>>`, `<<=`, `>>=`, `==`, `!=`, `<=`, `>=`, `++`, `--`, `%`, `&`, `^`, `!`, `|`, `~`, `&=`, `^=`, `|=`, `&&`, `||`, `%=`, `[]`, `()`, `,`, `->*`, `->`, `new`, `delete`, `new[]`, `delete[]`

```cpp
class CVector {
public:
    int x,y;
    CVector() {};
    CVector (int a, int b) : x(a), y(b) { }
    CVector operator + (const CVector&);
}

CVector CVector::operator+ (const CVector& param) {
    CVector temp;
    temp.x = x + param.x;
    temp.y = y + param.y;
    return temp;
}

int main() {
    CVector foo(3,1);
    CVector bar(1,2);
    CVector result;
    result = foo + bar;   // note that constructor is called three times:
                          // 1: CVector result;
                          // 2: CVector temp;
                          // 3: copy constructor in result = foo + bar;
                      // If we do CVector result = foo + bar;, we can reduce one constructor call
    cout << result.x << ',' << result.y << '\n';        // prints 4,3
    return 0;
}
```

<br>

## Static Instance Variables (or functions)

- Basically the same as Python
- Python: do not need `static` keyword

```cpp
class Dummy {
public:
    static int n;
    int instanceVar;
    Dummy() { n++; }
}

int Dummy::n=0;

int main() {
    Dummy a;
    Dummy b[5];
    cout << a.n << '\n';          // prints 6
    Dummy * c = new Dummy;
    cout << Dummy::n << '\n';     // prints 7
    delete c;
    return 0;
}
```

<br>

## `const`

- `const` applies to whatever lies on its immediate left; if it is the first thing of the line, then it applies to whatever is on its immediate right
- Constant values
  - `int const MIN_AGE = 21;`
  - `const int MIN_AGE = 21;`
- Pointer to constant value
  - `const int* p;`
- Constant pointer
  - `int* const p = &x;`
- Constant references
  - `CVector CVector::operator + (const CVector& param);`
- Constant methods
  - `int Loan::calcInterest() const { return loan_value * interest_rate; }`
  - Basically saying the method is only an accessor but not mutator; cannot change anything of the object
- Constant object instances
  - `const Loan myLoan;`
  - Only constructor/destructor can modify it
- How can a `const` method be used?
  - Const methods can always be called
  - Const method cannot call a non-const method
  - Non-const functions can only be called by non-const objects