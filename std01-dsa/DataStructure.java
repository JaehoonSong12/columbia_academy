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


public class DataStructure { // executable file (class)
    public static void main(String[] args) {
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
        List<Integer> numbers = new ArrayList<>();
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
        
        // TODO: 10. Convert 'numbers' to an Integer[] array and print its contents.

        // TODO: 11. Demonstrate ensureCapacity(20), then add 10 more elements.
        // TODO: 12. Trim the list to size and print the capacity hint (if possible).

        // TODO: 13. Add duplicates of number 5 into 'numbers'.
        // TODO: 14. Use indexOf(5) and lastIndexOf(5) and print both results.

        System.out.println();
    }
}




















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