// C++ program to demonstrate Static variables

#include <iostream>
using namespace std;

class MyClass
{

public:
    static int staticVariable;

    int instanceVariable;

    MyClass()
    {
        ++staticVariable;
    };

    void foo()
    {
        instanceVariable = 0;
    }
};

int MyClass::staticVariable = 0;

int main()
{
    MyClass obj1;
    obj1.instanceVariable = 10;

    cout << MyClass::staticVariable << endl;
    cout << obj1.instanceVariable << endl;

    MyClass obj2;
    obj2.instanceVariable = 20;

    cout << MyClass::staticVariable << endl;
    cout << obj2.instanceVariable << endl;
}
