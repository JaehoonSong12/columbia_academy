/**
INSTRUCTIONS: 
    Temporary space for Concepts and Test codes.



COMPILE & EXECUTE & CLEANUP (Java):

     javac  Main.java       # compile (.java to .class)
     java   Main            # execute (.class to run)
     rm     Main.class      # clean up .class files

    Note*: For Linux/macOS (using ':' as classpath separator) 

DEPENDENCIES: 
 */



public class Main {
    public static void main(String[] arg) { // static
        double z = 199.98; // local variable in "stack" (dynamic)
        Example instance = new Example(); // instance is local variable (pointer).
        System.out.println(instance.x);




        

        return;
    }
}

class Example {
    int x; // instantiated variable in "heap" (dynamic)
    static int y = 4;
}



/*

1. write code in human lang
2. compile it into binary (Compile-Time)
3. run the binary (Runtime)

static --- Compile Time (Translation)

dynamic (default without writing any) --- runtime


prmitive data? can be only defined in (1) code segment part or (2) stack, never in heap.
long
int
double
float


abstract data? 




 */