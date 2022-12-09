
// declare abstract class with "abstract"
abstract class Shape2D {
    protected int width, height;

    public Shape2D(int width, int height) {
        this.width = width;
        this.height = height;
    }

    // abstract method
    public abstract int area();
}


class Rectangle extends Shape2D {

    public Rectangle(int width, int height) {
        super(width, height);
    }

    public int area() {
        return width * height;
    }
}

class Triangle extends Shape2D {

    public Triangle(int width, int height) {
        super(width, height);
    }

    public int area() {
        return width * height / 2;
    }
}

public class abstract_classes {
    public static void main(String args[]) {

        // Leads to compile error: tries to create an instance of abstract class
        // Shape2D b = new Shape2D();


        Rectangle rect1 = new Rectangle(5, 7);
        System.out.println("Total Rectangle area: " + rect1.area());

        // alternative: declare with base type Shape2D
        Shape2D rect = new Rectangle(5, 7);
        System.out.println("Total Rectangle area: " + rect.area());
        // note: if Shape2D does not have area(), would throw error (even though constructor is for Rectangle)

        Triangle tri = new Triangle(5, 7);
        System.out.println("Total Triangle area: " + tri.area());

        // Demonstrate polymorphism while we're at it
        Shape2D[] arr = new Shape2D[2];

        arr[0] = rect;          // Rectangle object
        arr[1] = tri;           // Triangle object

        for (int i = 0; i < 2; i++)
            System.out.println("Total Shape area: " + arr[i].area());
    }
}