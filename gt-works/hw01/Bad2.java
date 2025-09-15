/*
INSTRUCTIONS:
    A PDF file is attached in the same folder.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw01/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw01/Bad2.java      # compile (.java to .class)
     java           -cp "./out"     Bad2                # execute (.class to run)
     rm -rf out/                                        # clean up .class files

DEPENDENCIES:
     None
 */

/**
 * This class is used to demonstrate bad coding practices #2.
 *
 * @author Taiyun Park
 * @version 0.0.1
 */
public class Bad2 {
    /**
     * Main method.
     *
     * @param args argument from user input
     */
    public static void main(String[] args) {
        int a = 1331;
        int b = 1;
        System.out.println("Welcome to \nCS 1331!");
        int c = a / b;
        System.out.println("c is equal to: " + c);
    }
}
