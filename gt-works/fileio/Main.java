/**
INSTRUCTIONS: 
    Homework1 is going on...
    
COLLABORATION: 
    I worked on the assignment alone, using only course-provided materials.

COMPILE & EXECUTE & CLEANUP (Java):

     javac  -d out                  fileio/Main.java      # compile (.java to .class)
     java           -cp "./out"     Main                # execute (.class to run)
     rm -rf out/                                        # clean up .class files
    
 */

import java.io.FileInputStream;
import java.io.FileOutputStream;

// import java.lang.Exception;
import java.io.File;
import java.io.IOException;                 // Exception: 
import java.io.FileNotFoundException;       // IOException > FileNotFoundException



import java.nio.charset.StandardCharsets;

// Python: raise ValueError

public class Main {
    public static void main(String[] args) {
        System.out.println("dsadsadsad");
        int x = 2;
        System.out.println("the value of x is: " + x);

        try {
            int y = 2 / 0;
        } catch (ArithmeticException e) {
            // TODO: handle exception
            System.out.println("Hey, you are making ArithmeticException (no need to be reported because this error is runtime error, not important error for your computer)");
        }


        // try {
            
        // } catch (Exception e) {
        //     // TODO: handle exception
        // }

        try {
            FileInputStream fileInputStream = new FileInputStream(new File("New Microsoft Word Document.docx"));
            int byteData;
            while ((byteData = fileInputStream.read()) != -1) {
                // Process the byteData (e.g., convert to char and print)
                System.out.print((char) byteData);
            }
        } catch (FileNotFoundException e) {
            System.out.println("FileNotFoundException");
        } catch (IOException e) {
            System.out.println("IOException");
        } catch (Exception e) {
            System.out.println("Exception");
        }







        try {
            FileOutputStream out = new FileOutputStream("output.txt");
            String personInput = "example string is here";
            byte[] bytes = personInput.getBytes(StandardCharsets.UTF_8);
            out.write(bytes);
        } catch (FileNotFoundException e) {
            // TODO: handle exception
            System.out.println("Hey, you are making FileNotFoundException (specific)");
        } catch (IOException e) {
            // TODO: handle exception
            System.out.println("Hey, you are making IOException (Mid)");
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Hey, you are making Exception (General)");
        }
        

    }
}