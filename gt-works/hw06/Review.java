/*
INSTRUCTIONS:
    A PDF file is attached in the same folder.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw06/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw06/Review.java    # compile (.java to .class)
     java           -cp "./out"     Review              # execute (.class to run)
     rm -rf out/                                            # clean up .class files

DEPENDENCIES:
 */
import java.util.Scanner;

/**
 * This class is homework 6.
 *
 * @author CS 1331 TAs
 * @version 1.0.0
 */
public class Review {
    /**
     * Main method for Review.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        MyData data1 = new MyData(5);
        MyData data2 = new MyData(10);
        if (data1.compareTo(data2) < 0) {
            System.out.println("data1 is less than data2");
        } else if (data1.compareTo(data2) > 0) {
            System.out.println("data1 is greater than data2");
        } else {
            System.out.println("data1 is equal to data2");
        }
        System.out.println(data1.compareTo(data2));
    }
}




/**
 * MyData class implementing Comparable interface.
 */
class MyData implements Comparable<MyData> {
    int value;
    /**
     * Constructor for MyData.
     *
     * @param v integer value
     */
    public MyData(int v) {
        value = v;
    }

    /**
     * Compares this MyData object with another MyData object.
     *
     * @param other another MyData object
     * @return 1 if this is greater, -1 if less, 0 if equal
     */
    @Override public int compareTo(MyData other) {
        if (other == null || this.value > other.value) return 1;
        if (this.value < other.value) return -1;
        return 0;
    }
}