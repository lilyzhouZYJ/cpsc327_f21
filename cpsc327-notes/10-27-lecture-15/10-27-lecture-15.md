# 10-27 Lecture 15

## `const`

```cpp
// constructor on const object
class MyClass {
public:
    int x;
    MyClass(int val) : x(val) {}
    int get() const { return x; }           // const member function
    const int& get() { return x; }          // member function returning const reference to int
    const int& get() const { return x; }    // const function returning const reference to int
};

int main() {
    const MyClass foo(10);
    // foo.x = 20;              // not valid!
    cout << foo.x << '\n';
    return 0;
}
```

<br>

## Passing References

```cpp
// C style
void duplicate1 (int * a, int * b, int * c){
    (*a) *= 2;
    (*b) *= 2;
    (*c) *= 2;
}

// C++ style
void duplicate2 (int& a, int & b, int & c){
    a *= 2;
    b *= 2;
    c *= 2;
}

// These functions do the same thing!
```

- *Note*: Python is a pass-by-reference language!

### Passing `const` References

- Ensure that the object passed in isn't mutated by the method

```cpp
// ensure the param would not be changed
CVector CVector::operator+ (const CVector& param)
```

<br>

## Templates

- Allows the type of a variable in a class to be decided during instantiation
- Same idea as generic types in Java (although done at compile time in C++)
- Unnecessary in Python

```cpp
template <class T>
class mypair {
    T a, b;
public:
    mypair (T first, T second)
        {a=first; b=second;}
    T getmax();
};

template <class T>
T mypair<T>::getmax() {
    T retval;
    retval = a > b ? a : b;
    return retval;
}

int main() {
    mypair <int> myobject(100, 75);
    cout << myobject.getmax();
    return 0;
}
```

<br>

## Destructor

- Called when an object is deleted
- Same name as constructor with `~` added to the beginning
- Clean up any dynamically allocated instance variables
- If no destructor is explicitly defined: default destructor - de-allocate the object, but does not delete any object the instance variables may point to

```cpp
class Example{
    string* ptr;
public:
    // constructors:
    Example(): ptr(new string) {}
    Example(const string& str) : ptr(new string(str)) {}
    // destructor
    ~Example() {delete ptr;}
    // access content:
    const string& content() const {return *ptr;}
};

int main() {
    Example foo;
    Example bar("Example");
    cout << "bar's content: " << bar.content() << '\n';
    return 0;

    // will automatically call destructor when exiting the scope
}
```

<br>

## Copy Constructor

- Used automatically when
  - Setting an object equal to another of the same type
  - Passing an object as an argument
  - Returning (if no move constructor)
- Implicit copy constructor used if you don't provide one
  - May or may not be a deep copy
  - Similar functionality exists in Python's copy package

```cpp
class Example {
    string* ptr;
public:
    Example (const string& str) : ptr(new string(str)) {}
    ~Example() {delete ptr;}
    // copy constructor
    Example(const Example& x) : ptr(new string(x.content())) {}
    // access content
    const string& content() const {return *ptr;}
};

int main() {
    Example foo("Example");
    Example bar = foo;

    cout << "bar's content: " << bar.content() << '\n';
    return 0;
}
```

<br>

## Implicit Special Functions

| Member function | Implicitly defined: | Default definition: |
| --------------- | ------------------- | ------------------- |
| **Default constructor** | If no other constructors | Does nothing |
| **Destructor** | If no destructor | Does nothing |
| **Copy constructor** | If no move constructor and no move assignment | Copies all members |
| **Copy assignment** | If no move constructor and no move assignment | Copies all members |
| **Move constructor** | If no destructor, no copy constructor, and no copy nor move assignment | Copies all members |
| **Move assignment** | If no destructor, no copy constructor, and no copy nor move assignment | Moves all members |

- **Copy constructor**
  - `Example foo = bar;`
- **Copy assignment**
  - If `foo` is already defined with `Example foo;`, then `foo = bar;` uses copy assignment
  - Basically copy constructor, but in two steps instead of one
- **Move constructor**
  - The old object no longer exists; it is moved to the new one
  - Usually what happens when functions return
- **Move assignment**
  - Moving into something that already exists; similar to copy assignment

<br>

## Inheritance

```cpp
class Polygon {
protected:
    int width, height;
public:
    void set_values (int a, int b)
    { width=a; height=b; }
};

class Rectangle: public Polygon {   // public inheritance
public:
    int area()
        { return width * height; }
};

class Triangle: public Polygon {
public:
    int area()
        { return width * height / 2; }
};

int main() {
    Rectangle rect;
    Triangle trg1;
    rect.set_values(4,5);
    trg1.set_values(4,5);
    cout << rect.area() << '\n';        // 20
    cout << trg1.area() << '\n';        // 10
    return 0;
}
```

- There is no `super` keyword in C++
- For those who like `super,` do this:

```cpp
private:
    typedef Mother super;
```

Alternative:

```cpp
class Mother{
public:
    Mother() {cout << "Mother: no parameters\n"; }
    Mother(int a) {cout << "Mother: int parameter\n"; }
};

class Daughter : public Mother{
public:
    Daughter (int a) {cout << "Daughter: int parameter\n"; }
    // constructor will still implicitly call Mother()
}

class Son: public Mother {
public:
    Son(int a): Mother(a)           
        { cout << "Son: int parameter\n"; }
        // since we are calling Mother with arguments, need to do so explicitly.
        // like calling super.__init__(a), but need to say name of parent class
}

// output:
// Mother: no parameter
// Daughter: int parameter
// Mother: int parameter
// Son: int parameter
```

<br>

## Polymorphism

```cpp
class Polygon {
protected:
    int width, height;
public:
    void set_values (int a, int b)
        {width=a; height=b;}
};

class Rectangle : public Polygon {
public:
    int area()
        {return width*height;}
};

class Triangle : public Polygon {
public:
    int area()
        {return width*height/2;}
};

int main() {
    Rectangle rect;
    Triangle trg1;
    Polygon* ppoly1 = &rect;
    Polygon* ppoly2 = &trg;
    ppoly1->set_values(4,5);
    ppoly2->set_values(4,5);
    // ppoly1->area();              // CANNOT DO THIS! Not defined for Polygon class
    cout << rect.area() << '\n';    // can do this
}
```

<br>

### **With Virtual Method**

```cpp
class Polygon {
protected:
    int width, height;
public:
    void set_values (int a, int b)
        {width=a; height=b;}
    virtual int area()      // virtual method in parent
        { return 0; }
};

class Rectangle : public Polygon {
public:
    int area()
        {return width*height;}
};

class Triangle : public Polygon {
public:
    int area()
        {return width*height/2;}
};

int main() {
    Rectangle rect;
    Triangle trg1;
    Polygon poly;
    Polygon* ppoly1 = &rect;
    Polygon* ppoly2 = &trg;
    Polygon* ppoly3 = &poly;
    ppoly1->set_values(4,5);
    ppoly2->set_values(4,5);
    ppoly3->set_values(4,5);
    cout << ppoly1->area() << '\n';     // CAN DO THIS NOW;
                                        // will call most specific version of area()
    cout << ppoly3->area() << '\n';     // will return 0
}
```

<br>

### **C++ Inheritance Access Specifier**

| Access specifier in base class | Access specifier when inherited publicly | Access specifier when inherited privately | Access specifier when inherited protectedly |
| -- | -- | -- | -- |
| Public | Public | Private | Protected |
| Protected | Protected | Private | Protected |
| Private | Inaccessible | Inaccessible | Inaccessible |

- Public inheritance does not modified the access modifiers of the base class
- Private ones are never inherited

<br>

## Moving on to Design...

- So far:
  - Classes
  - Association
  - Composition
  - Inheritance
  - Manager objects

<br>

## Design Patterns (starting chapter 9)

- General solutions to commonly occurring problems
- Not finished code, but rather a template
- Applicable to many different languages
  - Implementation may look different
  - The pattern might be built into the language like iterator in python

<br>

## History

- Design patterns became popular in the 1990s
- Software was rapidly becoming more complex
- Design patterns: elements of reusable object-oriented software
  - 1994
  - "Gang of Four"
  - Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides

<br>

## Why Learn Design Patterns?

- Re-using patterns can speed up development
- Less likely you need to refactor later
- Make code more readable to others who know the pattern
- Build up a vocabulary to communiate designs with other developers/managers

<br>

## Categories

- **Creational**
  - Ways to manage creation of objects
- **Structural**
  - Organizing classes and objects to provide new functionality
- **Behavioral**
  - Manage communication between objects
- **Concurrency**
  - Address challenges in multi-threading/multi-processing

<br>

## Iterator Pattern (Chapter 9)

- **Behavioral** pattern
- An iterator object is created to traverse elements from another object
- Traverse without exposing internal structure/representation
- Add new iterator for new traversal methods without changing the original object's interface
- Iterators are a common object-oriented pattern
- Classic:
  - `for(int i = 0; i < 10; i++) printf("%d\n", arr[i]);`
- Iteration is controlled externally
- General iterator pattern
  - `while not iterator.done(): print(iterator.next())`
- Iteration controlled internally