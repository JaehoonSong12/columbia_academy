 /**
 * This is a simple Java program that prints "Hello, World!" to the console.
 * 
 * How to compile and run the application:
 * 1. Open a terminal or command prompt.
 * 2. Compile (.java to .class): 
 *      ```
 *      javac std01-taiyun/Main.java
 *      ```
 * 3. Run & Clean (.class files are interpreted by JVM (java ~~~)): 
 *      ```
 *      java -cp std01-taiyun Main
 *      rm -rf std01-taiyun/*.class
 *      ```
 * 4. Documentation:
 *      ```
 *      javadoc -d std01-taiyun -sourcepath std01-taiyun Main.java
 *      javadoc -d /home/html -sourcepath std01-taiyun
 *      ```
 */

import java.util.Scanner; // Python: input()

class Main {
    public static void main(String[] args) {
        // name = input("what is your name?")
        // print(name)

        Scanner inputStream = new Scanner(System.in);
        // 1. always declare data type (static-typeing**, dynamic-typing in python)
        // 2. JRE offers you systemical built-in object, System.in == "system's keyboard", System.out == "system's cli or monitor" 
        // 3. 
        System.out.print("What is your name? "); // without ending == print("What is your name?", end="") in python
        String userName = inputStream.nextLine();
        // PascalCase
        // camelCase
        String formattedString = String.format("Hello, %s!", userName); // formattedString = f"Hello, {userName}!"
        System.out.println(formattedString); // print(formattedString)




        System.out.println("Hello, World!"); // newline-ending == print("Hello, World?") in python
    }
}