/*
INSTRUCTIONS:
    A PDF file is attached in the same folder.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw01/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw01/PrimitiveOperations.java   # compile (.java to .class)
     java           -cp "./out"     PrimitiveOperations             # execute (.class to run)
     rm -rf out/                                                    # clean up .class files

DEPENDENCIES:
     None
 */

/**
 * This class is a classwork for primitive operations.
 *
 * @author Taiyun Park
 * @version 0.0.1
 */
public class PrimitiveOperations {
    /**
     * Main method.
     *
     * @param args argument from user input
     */
    public static void main(String[] args) {
        int spongebobIQ = 5;
        double patrickIQ = 3.5;

        System.out.println(spongebobIQ);
        System.out.println(patrickIQ);

        double einsteinIQ = spongebobIQ * patrickIQ;
        System.out.println(einsteinIQ);

        double spongebobIQDouble = (double) spongebobIQ;
        System.out.println(spongebobIQDouble);

        int patrickIqInt = (int) patrickIQ;
        System.out.println(patrickIqInt);

        char favoriteLetter = 'E';
        System.out.println(favoriteLetter);

        char lowerChar = (char) (favoriteLetter + 32);
        System.out.println(lowerChar);
    }
}
