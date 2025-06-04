 /**
 * This is a simple Java program that prints "Hello, World!" to the console.
 * 
 * How to compile and run the application:
 * 1. Open a terminal or command prompt.
 * 2. Compile (.java to .class): 
 *      ```
 *      javac std01-taiyun/Main.java
 *      ```
 * 3. Run & Clean (.class files are interpreted by JVM (java ~~~)): 
 *      ```
 *      java -cp std01-taiyun Main
 *      rm -rf std01-taiyun/*.class
 *      ```
 * 4. Documentation:
 *      ```
 *      javadoc -d std01-taiyun -sourcepath std01-taiyun Main.java
 *      javadoc -d /home/html -sourcepath std01-taiyun
 *      ```
 */

import java.util.Scanner; // Python: input()

public class Main {
    /**
     * Abstraction (Procedural-oriented Programming#0)
     * - Once you implement a function, you do not have to know how it works.
     */
    static String hi(String input) {
        System.out.println("Hi " + input);
        return "Hi " + input;
    }





    public static void main(String[] args) {
        // // name = input("what is your name?")
        // // print(name)

        // Scanner inputStream = new Scanner(System.in);
        // // 1. always declare data type (static-typeing**, dynamic-typing in python)
        // // 2. JRE offers you systemical built-in object, System.in == "system's keyboard", System.out == "system's cli or monitor" 
        // // 3. 
        // System.out.print("What is your name? "); // without ending == print("What is your name?", end="") in python
        // String userName = inputStream.nextLine();
        // // PascalCase
        // // camelCase
        // String formattedString = String.format("Hello, %s!", userName); // formattedString = f"Hello, {userName}!"
        // System.out.println(formattedString); // print(formattedString)


        // System.out.println("Hello, World!"); // newline-ending == print("Hello, World?") in python






        MyData instance = null;
        MyData instance2 = null;
        instance = new MyData("Tayiun", 17);
        instance2 = new MyData("Jaehoon", 28);

        instance.report();
        instance.report;
        System.out.println(instance.report);
        instance2.report();

    }
}



// our own data type (ADT: Abstract Data Type, not primitive type)
/**
 * Encapsulation (OOP#1)
 * - having several 
 *      - fields (variables in a class)
 *      - methods (functions in a class)
 * in a single "class shell" ("Data type")
 */
class MyData {
    // (2) Fields are created in "heap"
    String name;
    int age;
    String report;
    // Constructor (special method for "new" to encapsulate data passed from outside)
    MyData(String name, int age) { // (1) params are created in "stack"! not in "heap"
        this.name = name; // (3) "this" keyword is to refer to fields in heap of "this" class!
        this.age = age;
        this.report = "This is default value, hi there";
    }
    // methods
    void report() {
        System.out.println(String.format("%s is %d years old!", name, age));
        return;
    }


}

// class String {
//     void format(String formatter, String[] args ...) {
//         // lexical analysis -> ADT (abstract ??? tree)
//         for (// each % substring 
//         ) {
//             // subsitutde the value from args.
//         }
//     }
// }