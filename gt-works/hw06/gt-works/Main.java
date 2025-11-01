/**
INSTRUCTIONS: 
    Temporary space for Concepts and Test codes.



COMPILE & EXECUTE & CLEANUP (Java):
1
    Note*: For Linux/macOS (using ':' as classpath separator) 

DEPENDENCIES: 
 */

java.lang.Object;

class Person extends Object {
    String name;
    private int age;
    public int getAge() { // accessor (you can get private data)
        return age;
    }

    Person() { // default constructor
        super();
        this("Unknown", 0);
    }

    Person(String name) { // constructor is called when you "new"  an object
        this(name, 0);
    }

    Person(String name, int age) { // constructor is called when you "new"  an object
        this.name = name;
        this.age = age;
    }

    void introduce() {
        System.out.println("Hello, I'm " + name + ", and I'm " + age + " years old.");
    }

    @Override public int toString() {
        return "Person{name='" + name + "', age=" + age + "}";
    }
    @Override public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj instanceof Person == false) return false;
        Person person = (Person) obj;
        return age == person.age && name.equals(person.name);
    }
}



public class Main {

    int a = 10; // instance variable in "heap" (dynamic)
    public static int b = 20; // static variable in "code segment" (static)


    public static void main(String[] arg) { // static
        // double z = 199.98; // local variable in "stack" (dynamic)
        // Example instance = new Example(); // instance is local variable (pointer).
        // System.out.println(instance.x);


        Person p1 = new Person();
        Person p2 = new Person("Unknown", 0);



        p1.name = "Alice";
        p1.age = 30;
        p1.introduce();

        // Person alice = new Person("Alice", 30);
        // alice.introduce();
        // Person bob = new Person("Bob", 25);
        // bob.introduce();
        // Person charlie = new Person("Charlie", 35);
        // charlie.introduce();

        hi(10); // int
        hi(10.5); // double
    }

    static void hi(int x) {
        System.out.println("hi int " + x);
    }
    static void hi(double x) {
        System.out.println("hi double " + x);
    }



}













class Example {
    int x; // instantiated variable in "heap" (dynamic)
    static int y = 4;
}



/*

1. write code in human lang
2. compile it into binary (Compile-Time)
3. run the binary (Runtime)

static --- Compile Time (Translation)

dynamic (default without writing any) --- runtime


prmitive data? can be only defined in (1) code segment part or (2) stack, never in heap.
long
int
double
float


abstract data? 




 */