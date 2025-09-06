/**
INSTRUCTIONS: 
    Homework1 is going on...
    
COLLABORATION: 
    I worked on the assignment alone, using only course-provided materials.

COMPILE & EXECUTE & CLEANUP (Java):

     javac  -d out                  hw01/StringOperations.java      # compile (.java to .class)
     java           -cp "./out"     StringOperations                # execute (.class to run)
     rm -rf out/                                        # clean up .class files
    
 */
public class StringOperations {
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
