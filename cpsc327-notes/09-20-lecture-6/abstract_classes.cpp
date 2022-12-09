#include <iostream>

using namespace std;

// Base class
class Shape2D {
public:
    // pure virtual function providing interface framework.
    virtual int area() = 0;
    Shape2D(int w, int h): width(w), height(h) {
    }

protected:
    int width;
    int height;
};

// Derived classes
class Rectangle : public Shape2D {
public:
    Rectangle(int w, int h): Shape2D(w, h) {

    }

    int area()
    {
        return width * height;
    }
};

class Triangle : public Shape2D {
public:
    Triangle(int w, int h): Shape2D(w, h) {

    }

    int area() {
        return width * height / 2;
    }
};

int main(void) {
    Rectangle rect(5, 7);
    Shape2D* rect2 = new Rectangle(5, 7);
    Triangle tri(5, 7);

    // Uncommenting the following line will cause compiler error as the
    // line tries to create an instance of abstract class.
    // Shape2D shp(5, 7);

    // Print the area of the object.
    cout << "Total Rectangle area: " << rect.area() << endl;
    cout << "Total Rectangle area: " << rect2->area() << endl;

    // Print the area of the object.
    cout << "Total Triangle area: " << tri.area() << endl;


    // Demonstrate polymorphism while we're at it
    Shape2D* arr[2];

    arr[0] = &rect;
    arr[1] = &tri;

    for (int i = 0; i < 2; i++) {
        cout << "Total Shape area: " << arr[i]->area() << endl;
    }

    return 0;
}