/**
INSTRUCTIONS: 
    Homework1 is going on...

COMPILE & EXECUTE & CLEANUP (Java):

     javac  -d out                  hw01/Bad2.java      # compile (.java to .class)
     java           -cp "./out"     Bad2                # execute (.class to run)
     rm -rf out/                                        # clean up .class files
    
 */
public class Bad2 {
    public static void main(String[] args) {
        int a = 1331;
        int b = 1;
        System.out.println("Welcome to \nCS 1331!");
        int c = a / b;
        System.out.println("c is equal to: " + c);
    }
}
