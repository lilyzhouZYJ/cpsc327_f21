// Interface
interface Shape2D {                     // interface cannot have constructor
    public abstract int area();
}

// Interface
interface Drawable {
    public abstract void draw();
    public abstract int area();
    // note the name collision with Shape2D, but this is okay
    // since interfaces do not have implementations
}

// Class implementing multiple interfaces
class Rectangle implements Shape2D, Drawable {
    protected int width, height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int area() {
        return width * height;
    }

    public void draw() {
        // do stuff
    }
}

class Triangle implements Shape2D {
    protected int width, height;

    public Triangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int area() {
        return width * height / 2;
    }
}


public class interfaces {
    public static void main(String args[]) {

        // Uncommenting the following line will cause compiler error as the
        // line tries to create an instance of abstract class.
        // Shape2D b = new Shape2D();

        // We can have references of Base type
        // even though Base type (Shape2D) is interface
        Shape2D rect = new Rectangle(5, 7);
        System.out.println("Total Rectangle area: " + rect.area());

        Triangle tri = new Triangle(5, 7);
        System.out.println("Total Triangle area: " + tri.area());

        // Demonstrate polymorphism while we're at it
        Shape2D[] arr = new Shape2D[2];

        arr[0] = rect;
        arr[1] = tri;

        for (int i = 0; i < 2; i++) {
            System.out.println("Total Shape area: " + arr[i].area());
        }

    }
}