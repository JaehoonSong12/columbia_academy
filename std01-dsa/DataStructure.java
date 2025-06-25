/**
 * The DataStructure class demonstrates the implementation of a dynamic array (ArrayListX)
 * and a set (ArraySet) with custom behaviors.
 * <p>
 * It includes methods to perform basic list operations such as add, get, remove, and contains,
 * as well as set-specific operations like union and intersection. The ArraySet class extends
 * ArrayListX to enforce set semantics by preventing duplicate elements.
 * </p>
 * 
 * How to compile and run the application:
 * 1. Open a terminal or command prompt.
 * 2. Compile: 
 *      ```
 *      javac std01-dsa/DataStructure.java
 *      ```
 * 
 * 3. Run & Clean: 
 *      ```
 *      java -cp std01-dsa DataStructure; rm -rf std01-dsa/*.class
 *      ```
 */

import java.util.List;
import java.util.ArrayList;
import java.lang.reflect.Field;


public class DataStructure { // executable file (class)
    public static void main(String[] args) {


        // // Box for Integer
        // Box<Integer> intBox = new Box<>();
        // intBox.set(123);
        // System.out.println("Integer Value: " + intBox.get());

        // // Box for String
        // Box<String> strBox = new Box<>();
        // strBox.set("Hello Generics!");
        // System.out.println("String Value: " + strBox.get());

        // Box<Person> personBox = new Box<>();
        // personBox.set(new Person("Jaehoon", 28));
        // System.out.println("Person Value: " + personBox.get());



        /**
         * Try it by yourself
         */
        System.out.println("--- ArrayList Activity ---\n");
        basicOperations();
        advancedOperations();
    }



    /**
     * Practice basic ArrayList operations: add, get, set, remove, contains, size.
     */
    private static void basicOperations() {
        System.out.println("1. Basic Operations");
        // TODO: 1. Declare an ArrayList of Strings named 'fruits'.
        List<String> fruits = new ArrayList<>();
        //       2. Add "Apple", "Banana", "Cherry" to the list.
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");
        //       3. Print the list.
        System.out.println(fruits); // toString <-- is called when you put it into System.out.println
        // TODO: 4. Get the element at index 1 and print it.
        System.out.println(fruits.get(1));
        // TODO: 5. Change the element at index 2 to "Blueberry" using set().
        fruits.set(2, "Blueberry");
        // TODO: 6. Remove the element "Apple" by value.
        fruits.remove(0);
        // TODO: 7. Check if the list contains "Cherry" and print the result.
        System.out.println("the list contains 'Cherry'? " + fruits.contains("Cherry"));
        // TODO: 8. Print the size of the list.
        System.out.println(fruits.size());
        System.out.println();
    }

    /**
     * Practice more advanced ArrayList methods: 
     * addAll, removeAll, retainAll,
     * subList, toArray, ensureCapacity, 
     * trimToSize, indexOf, lastIndexOf.
     */
    private static void advancedOperations() {
        System.out.println("2. Advanced Operations");
        // TODO: 1. Create an ArrayList<Integer> named 'numbers'.
        List<Integer> numbers = new ArrayList<>(); //  // Up-casting (from child to Parent)
        ////////// nubmers : List<Integer>
        ///   inheritance: List (Parent), ArrayList (Child)
        ///  Child is a Parent <---- "polymorphism"
        /// 
        //       2. Add the integers 1 through 5 using a loop or addAll().
        for (int i = 1; i <= 5; i++) {
            numbers.add(i);
        }
        // TODO: 3. Create another List<Integer> named 'moreNums' containing 4,5,6,7.
        List<Integer> moreNums = new ArrayList<>();
        for (int i = 4; i <= 7; i++) {
            moreNums.add(i);
        }


        // E.C.
        // for (var element: moreNums) { // read-only (usages)
        //     element = 999;
        // }
        // System.out.println(moreNums);


        // TODO: 4. Add all elements from 'moreNums' to 'numbers'.
        for (int i = 0; i < moreNums.size(); i++) {
            numbers.add(moreNums.get(i));
        }
        // TODO: 5. Print 'numbers'.
        System.out.println(numbers);
        // TODO: 6. Remove all elements in 'moreNums' from 'numbers' using removeAll().
        //       Print the list again.
        numbers.removeAll(moreNums); // subject.verb(objective)
        System.out.println(numbers);
        // TODO: 7. Add 2,3 back into 'numbers'.
        numbers.add(2);
        numbers.add(3);
        System.out.println(numbers);
        // TODO: 8. Use retainAll() to keep only elements that are in 'moreNums'.
        //       Print the list.
        numbers.retainAll(moreNums);
        System.out.println(numbers);
        // TODO: 9. Reset 'numbers' to 1-7, then get a subList from index 2 to 5.
        //       Print the subList.
        for (int i = 1; i <= 7; i++) {
            numbers.add(i);
        }
        List<Integer> sublist = new ArrayList<>(); // Generics (mod on existing class into specific type)
        // Integer is a class by JVM, not a standalone primitive data
        // java.lang.Object (needed for enabling "generics")
        //     java.lang.Number
        //         java.lang.Integer




        for (int i = 2; i <= 5; i++) {
            sublist.add(numbers.get(i));
        }
        System.out.println(sublist);
        // TODO: 10. Convert 'numbers' to an Integer[] array and print its contents.
        // int[] newArray = new int[numbers.size()];           // (primitive) array of int values
        Integer[] newArray = new Integer[numbers.size()];   // (abstract) array of addresses of Integer Object
        
        System.out.println("Printing.... before assignment");
        for (int i = 0; i < newArray.length; i++) {
            System.out.print(newArray[i] + ", "); // printing each element of newArray
        }
        System.out.println(); // printing extra line
        System.out.println("Printing.... after assignment");
        for (int i = 0; i < newArray.length; i++) {
            newArray[i] = numbers.get(i);
            System.out.print(newArray[i] + ", "); // printing each element of newArray
        }
        System.out.println(); // printing extra line
        System.out.println(numbers); // printing the entire list of "numbers"
        
        // TODO: 11. Demonstrate ensureCapacity(20), then add 10 more elements.
        ((ArrayList<Integer>) numbers).ensureCapacity(20); // Down-casting
        // 
        for (int i = 1; i <= 10; i++) {
            numbers.add(i);
        }
        System.out.println(numbers); 
        // [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, (0, 0, 0)], capacity == 20
        // TODO: 12. Trim the list to size and print the capacity hint (if possible).
        ((ArrayList<Integer>) numbers).trimToSize();
        System.out.println(numbers);
        
        ((ArrayList<Integer>) numbers).ensureCapacity(10); // Down-casting
        // [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], capacity == 17
        System.out.println(numbers);





        // TODO: 13. Add duplicates of number 5 into 'numbers'.
        // TODO: 14. Use indexOf(5) and lastIndexOf(5) and print both results.

        System.out.println();
    }
}




/**
 * < Timeline of Dev >
 * 1. Design your own class.
 *      - "Generics" helps you to decidce "data type" to use for some class/methods in compile-time
 * 
 * List<Integer> arr = new ArrayList<>();
 * List<Double> arr = new ArrayList<>();
 * List<String> arr = new ArrayList<>();
 * 
 * int[] arr = new int[10];
 * double[] arr = new double[100];
 * String[] arr = new double[100];
 * 
 * 2. Use them in your code - "compile-time"
 * 3. All the codes are running, and functions are working, sometime error shows up - "runtime"
 */

// Define a generic class
class Box<T extends Object> { // T: type parameter <- data type decided at compile-time
    private T value;
    public void set(T value) {
        this.value = value;
    }
    public T get() {
        return value;
    }
}

// Integer is a class by JVM, not a standalone primitive data
// java.lang.Object (needed for enabling "generics")
//     java.lang.Number
//         java.lang.Integer




























// ArrayListX is specifically designed for `double` data type so it is equivalent to 
//  ```
//  ArrayList<Double>
//  ```
class ArrayListX extends Object { 
    protected double[] arr;
    protected int size;
    private static final int defaultSize = 16;

    public ArrayListX() { // no-args constructor
    }
    public ArrayListX(double[] arr, int size) {
    }


    @Override // Override
    public String toString() {
        return super.toString();
    }



    public int size() { return 0; }
    public boolean isEmpty() { return false; }

    public boolean add(double element) {
        return false; 
    } // Overload
    public boolean add(int index, double element) {
        return false; 
    }
    private void resize() {
        return;
    }

    public double remove(double element){
        return 0.0;
    } //overload
    public double remove(int index) {
        return 0.0;
    }
    
    public boolean set(int index, double element){
        return false; 
    }
    
    public double get(int index){
        return 0.0;
    }

    public boolean contains(double element){
        return false; 
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
class Student extends Person{
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


