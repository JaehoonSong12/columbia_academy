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

class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}