/**
INSTRUCTIONS: 
    Homework1 is going on...
    
COLLABORATION: 
    I worked on the assignment alone, using only course-provided materials.

COMPILE & EXECUTE & CLEANUP (Java):

     javac  -d out                  fileio/Main.java      # compile (.java to .class)
     java           -cp "./out"     Main                # execute (.class to run)
     rm -rf out/                                        # clean up .class files
    
    Note*: For Linux/macOS (using ':' as classpath separator) 

DEPENDENCIES: 
 */
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

import javafx.application.Application;      // the Chrome Browser for example

import javafx.stage.Stage;                  // the Chrome Browser Window (the top-level container)

import javafx.scene.Scene;                  // the webpage in the browser window


import javafx.scene.layout.*;           // UI components > Layouts (Containers)


import javafx.scene.control.Label;          // UI components > Control
import javafx.scene.control.TextField;      // UI components > Control
import javafx.scene.control.Button;         // UI components > Control



import javafx.event.EventHandler;
import javafx.event.ActionEvent;            // abstraction is very high, so you don't need to know much details


/*
 * 1. Functional Interface: encapsulate a single abstract method (SAM) as a data.
 * 2. Lambda Expression: provide the implementation of the abstract method of a functional interface.
 * 
 */

// Taiyun ------->(verb? action verb? == method)->------ Computer (Button)



public class Main extends Application {
    public static void main(String[] args) {
        launch(args); // JavaFX application launch
    }

    Label label;
    private TextField textField;
    Button button;

    @Override public void start(Stage stage) {
        // label, textfield, button, so everytime the button is clicked, the text in the label changes to what is in the textfield
        label = new Label("Enter your name:");
        textField = new TextField();
        button = new Button("Submit");

        button.setOnAction((event) -> { // 
            String name = textField.getText();
            label.setText("Hello, " + name + "!");
        });
        




        // algorithm
        double[] array = {5.0, 3.0, 8.0, 1.0, 4.0, 7.0, 2.0, 6.0, 0.0, 9.0, 12.0, 11.0, 10.0};
        double[] outputArray = Algo.mergeSort(array);

        List<Double> list = new ArrayList<>();
        for (double num : outputArray) list.add(num);


        Label cliOutput = new Label();
        cliOutput.setText(list.toString());




        HBox hbox = new HBox(10, textField, button); // spacing of 10 pixels
        VBox vbox = new VBox(10, cliOutput, label, hbox); // spacing of
        Scene scene = new Scene(vbox, 300, 100); // width: 300, height: 100
        stage.setScene(scene);
        stage.setTitle("Hello JavaFX");
        stage.show();
    }

}




class Algo {
    /**
     * Time Complexity: O(n log n)
     */
    public static double[] mergeSort(double[] array) {
        // base case, O(1) constant time.
        if (array.length <= 2) {
            if (array.length == 2 && array[0] > array[1]) {
                double temp = array[0];
                array[0] = array[1];
                array[1] = temp;
            }
            return array;
        }
        // reduction step, O(n) linear time.
        int mid = array.length / 2;
        double[] left = new double[mid];
        double[] right = new double[array.length - mid];

        int lIndex = 0;
        int rIndex = 0;
        for (int i = 0; i < array.length; i++) {
            if (i < mid) left[lIndex++] = array[i];
            else right[rIndex++] = array[i];
        }
        
        // recursive call, O(log n) logarithmic time.
        left = mergeSort(left);
        right = mergeSort(right);

        // merge, O(n) linear time.
        int i = 0;
        lIndex = 0;
        rIndex = 0;
        while(i < array.length) { // comparison
            if (lIndex == left.length || rIndex == right.length)        break;
            if      (left[lIndex] <= right[rIndex])                     array[i++] = left[lIndex++];
            else if (left[lIndex] > right[rIndex])                      array[i++] = right[rIndex++];
        }
        if (lIndex == left.length)  while (rIndex < right.length)       array[i++] = right[rIndex++]; // drain the right side
        if (rIndex == right.length) while (lIndex < left.length)        array[i++] = left[lIndex++];  // drain the left side
        return array;
    }
}






// L18: Recursion (or Repetition Part 2)

//     Recursion: what it is, the three components (terminating condition / base case, reduction step, recursive call)
//     Recursion: Writing recursive methods




//     Recursion tracing with call stack
//     StackOverflowError and when it could happen

















interface Visible { // Multiple inheritance

}
interface Speakable { // Multiple inheritance
    void speak(); // pulbic abstract by default
}

abstract class Animal extends Object { // Single inheritance
    protected int id; // accessible within package and subclasses

    public Animal() {
        System.out.println("An animal is created.");
    }

    @Override public String toString() {
        return "I am an animal.";
    }
}

class Person extends Animal implements Visible, Speakable, Comparable<Person> {
    public String comment;      // the largest scope
    protected int age;          // 2rd package-private and subclass (even from different package)
    double height;              // 3nd package-private (default)
    private final String name;  // 4th private to the class only

    public Person() { // default constructor (**auto, if no constructor is defined)
        super();
        this.name = "John Doe"; 
        // this("John Doe");
    }
    public Person(String name) {
        this.name = name;
        super.id = 100; // accessing superclass's protected member
    }

    @Override public void speak() {
        System.out.println("Hello, my name is " + name + ".");
    }

    @Override public String toString() {
        return super.toString() + "I am a person named " + name + ".";
    }
    @Override public boolean equals(Object obj) {
        if (obj == null) throw new NullPointerException("You are comparing it to null"); // null check
        if (!(obj instanceof Person)) throw new RuntimeException("Type mismatch"); // instanceof check
        Person other = (Person) obj; // down casting
        return this.name.equals(other.name);
    }
    @Override public int compareTo(Person other) {
        // if (this.age < other.age) return -1;
        // else if (this.age > other.age) return 1;
        // else return 0;
        return this.age - other.age;
    }

}




//     Generics and parameterized types
//     Arrays.sort
//     L13: Algorithms

//     General knowledge of big-O notation for runtime
//     Growth rate for common big-O notation (the ones covered in the course)
//     Big-O runtime (best case and worst case), growth rate, and searching/sorting behavior of the following:


//     linear search
//     binary search

//     selection sort
//     insertion sort
//     merge sort
//     Completing code (through fill-in-the-blank or multiple choice) for:
//     linear/binary search
//     selection/insertion sort
//     Writing code
//     linear search
//     You will NOT be required to code for binary search or any sorting algorithm completely from scratch
//     Notable advantages and/or inefficiencies of each algorithm
//     Identifying big-O runtime and growth rate of example scenarios/code



abstract class Dummy {
    // just a dummy class to test multiple classes in one file
    public abstract void sayHi1(int times);
    public abstract void sayHi2(double suffix);
}





// // functional programming (lambda expressions / Single Abstract Method)
// @FunctionalInterface
// interface BinaryOperation {
//     double operate(double a, double b);
// }

// // 1. abstract class
// // 2. interface
// // 3. @FunctionalInterface

// // All can be lambda expressions.















/**
 * L1 and L2: Java and OOP

Brief history of Java and its development
Why OOP?
What are classes?
What are objects?
Compiled language vs interpreted language
The compiler and interpreter in Java
    Advantage of using both a compiler and an interpreter
    What does the compiler do?
    What is the JVM?
Identifiers
    Reserved words
    Valid identifiers
Declaring and instantiating
    Java is statically-typed
Designing a class with relevant attributes and/or behaviors


L3 and L4: Basics

Errors
    Compiler errors vs. runtime errors
    Logical errors
    Difference between syntax and semantics
Variables and constants
    The scope of a variable
    Keywords (such as final)
Primitives
    All primitives and relative sizes in memory
    Legal assignment of literals
        Type conversion
        Widening vs. narrowing
        Casting
    Purpose of having multiple numerical primitive types
Primitive operations
    Order of operations
    Arithmetic operators
        Integer division
    Incrementing and decrementing
    Evaluating expressions
Assignment operators
    =
    +=, -=, *=, etc.
Strings
    String methods (such as those used in HW1)
    String "arithmetic"
    String constant pool
    String immutability
Predefined classes (such as String)
    Reference variables
        Aliases
        Garbage collection
    Instantiation using 'new' keyword
    Invoking methods


L5: Input and Output

Reading command line inputs with Scanner
    Instantiating a Scanner object
    hasNext()
    nextLine() vs. next()
Java packages
    java.lang package
    java.util package
    Importing a package
Formatting
    System.out.printf()
    String.format()
    DecimalFormat and NumberFormat
Short coding problems involving command line inputs


L6: Decision-making statements

if statement
    Multi-way branching with else if
    Conditional operator (ternary operator)
switch statement
    default statement
    break statement
equals() method
    String interning and String constant pool
compareTo() method
Logical operators
    ==, <, <=, >, etc.
    AND, OR, NOT
Short circuit evaluation
Tracing (for both switch and if statements)


L7: Iteration

    while loop
    do-while loop
    for loop
    initialization statement
    condition
    update statement
    Difference between break and continue
    Writing and tracing (for all the above)
    Converting between while and for loops
    
L8: Arrays

    What is an array?
    What can be stored in an array?
    Array instantiation
    Array length
    Default values
    Assigning to a literal array
    Accessing and changing individual elements
    for-each statement
    Array traversal and searching
    NullPointerException and null check
    Using break
    Ragged arrays
    Two-dimensional arrays
    Accessing and assigning
    Column-major traversal
    Row-major traversal
    Wrapper classes (such as Double)
    Arrays class


L9: Methods

Writing methods
Parts of a method header
return type
method name
formal parameters
other modifiers (public, static, etc.)
Keywords (such as return)
Method overloading


L10 and L11: Writing classes

    Instance variables
    Static variables
    Static methods and what they can access
    Visibility modifiers
    Encapsulation and its purpose
    Visibility for instance variables
    Visibility for constants
    Constructors
    Writing constructors
    Constructor header
    Using "this" as a reference
    Implicit default constructor and default values
    Invoking a constructor to instantiate an object
    Constructor chaining and this()
    Notable methods
    toString() method
    Accessors and mutators
    Knowing how to code both
    Static variables have static getters and setters
    Math.random()



L15: Polymorphism

    Declared type vs. object type
    Tracing
    Identifying which method will be invoked at runtime
    Identifying any compiler/runtime errors
    Legal assignments/casting
    Compile-time and runtime "is-a" checks
    Legal method calls
    Dynamic binding


L16: Exceptions

    Why exceptions?
    Call Stack & Call Stack Trace
    The Throwable hierarchy
    Exception
    RuntimeException
    Checked vs. unchecked exceptions
    Exception handling with try-catch-finally and propagation
    Writing
    Tracing
    Throwing exceptions
    Writing exception classes
    Notable exceptions
    FileNotFoundException, IOException, NullPointerException, ArrayIndexOutOfBoundsException, ArithmeticException, etc.

L16: File I/O
    File object
    Reading with Scanner
    Writing with PrintWriter
    Delimited files
    Tracing behavior of code that uses file I/O


L17: Lists (and more Generics)

    Lists and the List Interface
    Generic Classes: everything in 'Basics of Writing Generic Classes'
    Array List: what it is / how it behaves, creating (Java's), using (Java's)
    Linked List: what it is / how it behaves, creating (Java's), using (Java's)
    Linked List: Coding a Linked List using Generics
    Coding of a Node as a private inner class
    Coding of a LinkedList (HW9)
    We may also ask you to code methods that weren't present in HW9 to test your understanding of reading and manipulating the node structure
    Linked Lists vs. Array Lists
    (Private) Inner Classes




---
 */





















// import java.io.FileInputStream;
// import java.io.FileOutputStream;
// // import java.lang.Exception;
// import java.io.File;
// import java.io.IOException;                 // Exception: 
// import java.io.FileNotFoundException;       // IOException > FileNotFoundException



// import java.nio.charset.StandardCharsets;

// // Python: raise ValueError

// public class Main {
//     public static void main(String[] args) {
//         System.out.println("dsadsadsad");
//         int x = 2;
//         System.out.println("the value of x is: " + x);

//         try {
//             int y = 2 / 0;
//         } catch (ArithmeticException e) {
//             // TODO: handle exception
//             System.out.println("Hey, you are making ArithmeticException (no need to be reported because this error is runtime error, not important error for your computer)");
//         }


//         // try {
            
//         // } catch (Exception e) {
//         //     // TODO: handle exception
//         // }

//         try {
//             FileInputStream fileInputStream = new FileInputStream(new File("New Microsoft Word Document.docx"));
//             int byteData;
//             while ((byteData = fileInputStream.read()) != -1) {
//                 // Process the byteData (e.g., convert to char and print)
//                 System.out.print((char) byteData);
//             }
//         } catch (FileNotFoundException e) {
//             System.out.println("FileNotFoundException");
//         } catch (IOException e) {
//             System.out.println("IOException");
//         } catch (Exception e) {
//             System.out.println("Exception");
//         }







//         try {
//             FileOutputStream out = new FileOutputStream("output.txt");
//             String personInput = "example string is here";
//             byte[] bytes = personInput.getBytes(StandardCharsets.UTF_8);
//             out.write(bytes);
//         } catch (FileNotFoundException e) {
//             // TODO: handle exception
//             System.out.println("Hey, you are making FileNotFoundException (specific)");
//         } catch (IOException e) {
//             // TODO: handle exception
//             System.out.println("Hey, you are making IOException (Mid)");
//         } catch (Exception e) {
//             // TODO: handle exception
//             System.out.println("Hey, you are making Exception (General)");
//         }
        

//     }
// }

