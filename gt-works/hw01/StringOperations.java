/*
INSTRUCTIONS:
    A PDF file is attached in the same folder.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw01/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw01/StringOperations.java  # compile (.java to .class)
     java           -cp "./out"     StringOperations            # execute (.class to run)
     rm -rf out/                                                # clean up .class files

DEPENDENCIES:
     None
 */

/**
 * This class is a classwork for string operations.
 *
 * @author Taiyun Park
 * @version 0.0.1
 */
public class StringOperations {
    /**
     * Main method.
     *
     * @param args argument from user input
     */
    public static void main(String[] args) {
        String myName = "Tai";
        System.out.println(myName);

        String modifiedName = "A"
            + myName.substring(1, myName.length() - 1)
            + "Z";
        System.out.println(modifiedName);

        String website = "www.gatech.edu";
        System.out.println(website);

        int startIndex = 4;
        int endIndex = website.length() - 4;
        String siteName = website.substring(startIndex, endIndex);
        String siteNameWithNumber = siteName + "1331";
        System.out.println(siteNameWithNumber);
    }
}
