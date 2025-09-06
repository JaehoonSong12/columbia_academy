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
import java.util.List;
import java.util.ArrayList; // inheritance: ArrayList (child) "is-a" List (parent)

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








        /**
         * < 06/10/2025 >
         * 1. Review on OOP below. Try to add more classes, methods, and fields.
         * 2. Try to research some good library or language utility classes offered by Java.
         * 3. Use them for solving the 2 rest problems in AlgorithmAPFirst.java
         */



        // Polymorphism: use-cases of inheritance
        Person instance = null;
        Person instance2 = null;
        instance = new Student("Tayiun", 17, "2023-0001");
        instance2 = new Teacher("Jaehoon", 28, "Math/CS");

        System.out.println(instance); // instance.report();
        System.out.println(instance2); // instance2.report();
        // instance.report;
        // System.out.println(instance.report);
        instance.report();
        instance2.report();

        if (instance instanceof Student) ((Student) instance).getSumOfNumbers(new int[] {5, 6, 7});

        


        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(7);
        list.remove(0);
        System.out.println(list);
        List<Integer> list2 = new ArrayList<>();

        

    }
}









/**
 * Inheritance, to reduce code repetition. By inheriting from a 
 * root class (parent) to specific class (child)
 *                    parent
 *                    /     \
 *               Tayiun     Older brother
 */
class Person extends java.lang.Object { // Root (Super class) super
    String name;
    int age;
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return String.format("%s is %d years old,", this.name, this.age);
    }

    void report() {
        System.out.println(this.toString());
    }
}



class Teacher extends Person { // this.
    String subject;
    Teacher(String name, int age, String subject) {
        super(name, age); // super call: calling the constructor or method from parent.
        this.subject = subject;
    }
    @Override // re-defining behavior. super call: to inherit part of your parent class.
    public String toString() {
        return super.toString() + String.format(" and teaches %s!", this.subject);
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
class Student extends Person {
    // (2) Fields are created in "heap"
    String stdId;
    // Constructor (special method for "new" to encapsulate data passed from outside)
    Student(String name, int age, String stdId) { // (1) params are created in "stack"! not in "heap"
        super(name, age);
        this.stdId = stdId;  // (3) "this" keyword is to refer to fields in heap of "this" class!
    }
    // methods
    @Override
    public String toString() { // function signature (return type: String, function name: toString, args name: ()) must be same.
        return super.toString() + String.format(",,, Stduent ID: %s", this.stdId);
    }
    
    int getSumOfNumbers(int[] numbers) {
        int SumOfNumbers = 0;
        for (int i = 0; i < numbers.length; i++) {
            SumOfNumbers += numbers[i];
        }
        System.out.println(String.format("%d", SumOfNumbers));
        return 0;
    }
}







// import java.lang.*;

// from package.seomthing import function 
// <- you always have class shell, so standalone function not allowed.

// package java.lang; // String is in java.lang package, so you do not need to import it

// class String {
//     void format(String formatter, String[] args ...) {
//         // lexical analysis -> ADT (abstract ??? tree)
//         for (// each % substring 
//         ) {
//             // subsitutde the value from args.
//         }
//     }
// }