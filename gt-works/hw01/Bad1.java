/**
INSTRUCTIONS: 
    Homework1 is going on...
    
COLLABORATION: 
    I worked on the assignment alone, using only course-provided materials.

COMPILE & EXECUTE & CLEANUP (Java):

     javac  -d out                  hw01/Bad1.java      # compile (.java to .class)
     java           -cp "./out"     Bad1                # execute (.class to run)
     rm -rf out/                                        # clean up .class files
    
 */
public class Bad1 {
    public static void main(String[] args) {
        String str = new String("CS1331ROCKS");
        System.out.println(str.length() - 5 + " is 11 - 5");
    }
}