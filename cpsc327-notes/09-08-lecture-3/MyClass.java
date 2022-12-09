
public class MyClass {
    public static int staticVariable = 0;

    public int instanceVariable;

    public MyClass(int x) {
        this.instanceVariable = x;
        staticVariable++;
    }

    public static void static_method(int x) {
        staticVariable = 5;
    }

    public static void main(String[] args) {
        MyClass obj1 = new MyClass(10);

        System.out.println(MyClass.staticVariable);
        System.out.println(obj1.instanceVariable);

        MyClass obj2 = new MyClass(20);

        System.out.println(MyClass.staticVariable);
        System.out.println(obj2.instanceVariable);
    }
}
