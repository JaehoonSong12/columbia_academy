 /**
 * This is a simple Java program that prints "Hello, World!" to the console.
 * 
 * How to compile and run the application:
 * 1. Open a terminal or command prompt.
 * 2. Compile (.java to .class): 
 *      ```
     javac Main.java
 *      ```
 * 3. Java Archieve & Run & Clean (.class files are interpreted by JVM (java ~~~)): 
 *      ```
     jar cfe Main.jar Main Main*.class
     java -jar Main.jar
     rm -rf *.class *.jar
        ```
 */


/*

     javac Main.java
     jar cfe Main.jar Main Main.class
     java -jar Main.jar
     rm -rf *.class *.jar

 */



import java.util.Scanner;


import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;



public class Main {
    public static void main(String[] args) {

        
        Scanner input = new Scanner(System.in);

        // System.out.print("Enter the radius of the circle in meters: ");
        // double radius = input.nextDouble();


        // final double PI = 3.14159;
        // double area = PI * radius * radius;
        // // f"The area of a circle with radius {radius} is {area}"
        // System.out.println(String.format(
        //     "The area of a circle with radius %.2f m is %.2f m^2",
        //     radius,
        //     area
        // ));


        // 
        System.out.println("This is a Temperature Converter Program....");
        System.out.println("Choose Fahrenheit or Celsius. Enter F or C");
        char choice = input.next().toUpperCase().charAt(0);
        double degreeInFahrenheit = -1;
        double degreeInCelsius = -1;
        System.out.println("You have chosen " + choice);
        
        if (choice == 'F') {
            System.out.println("Enter the degrees rounded to the nearest integer.");
            degreeInFahrenheit = input.nextDouble();
            degreeInCelsius = (degreeInFahrenheit - 32) * 5 / 9;
        } else if (choice == 'C') {
            System.out.println("Enter the degrees rounded to the nearest integer.");
            degreeInCelsius = input.nextDouble();
            degreeInFahrenheit = (degreeInCelsius * 9 / 5) + 32; 
        } else {
            System.out.println("Invalid choice. Please enter F or C.");
        }

        
        System.out.println(String.format(
            "That's %.2f degrees in Fahrenheit and %.2f degrees in Celsius!",
            degreeInFahrenheit,
            degreeInCelsius
        ));
        System.out.println("Thank you for using the Temperature Converter Program!");
        
        





        // hi_there // snake case
        // hiThere // camel case //variable
        // HiThere // pascal case //class name




        // adjust seed to Estern Standard Time (EST) with locale
        

        // Obtain the total milliseconds since midnight, Jan 1, 1970
        long totalMilliseconds = System.currentTimeMillis();
        

        System.out.println("Total milliseconds since midnight, Jan 1, 1970: " + totalMilliseconds);

        // Obtain the total seconds since midnight, Jan 1, 1970
        long totalSeconds = totalMilliseconds / 1000;
        // Compute the current second in the minute in the hour
        long currentSecond = totalSeconds % 60;
        // Obtain the total minutes
        long totalMinutes = totalSeconds / 60;
        // Compute the current minute in the hour
        long currentMinute = totalMinutes % 60;
        // Obtain the total hours
        long totalHours = totalMinutes / 60;
        // Compute the current hour
        long currentHour = totalHours % 24;
        // Display results
        System.out.println(
            String.format(
                "Current time is %02d:%02d:%02d GMT",
                currentHour,
                currentMinute,
                currentSecond
            )
        );





        Date currentDate = new Date(System.currentTimeMillis());

        // Format the date in Eastern Standard Time (EST)
        SimpleDateFormat sdfEST = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss z");
        sdfEST.setTimeZone(TimeZone.getTimeZone("America/New_York")); // Use a specific region ID

        System.out.println("Date in EST: " + sdfEST.format(currentDate));
    



        // *3.33




        // activity
        


    }
}
// https://docs.oracle.com/javase/8/docs/api/java/lang/String.html

/*
| Specifier | Data Type | Description | Example Code | Output |
| :--- | :--- | :--- | :--- | :--- |
| %s | String | Formats a string. | String.format("Hello %s", "world") | Hello world |
| %d | Integer | Formats a decimal integer. | String.format("The number is %d", 42) | The number is 42 |
| %f | Floatingpoint | Formats a decimal number (float or double). | String.format("Price: %.2f", 12.998) | Price: 13.00 |
| %b | Boolean | Formats a boolean as "true" or "false". | String.format("Is active: %b", true) | Is active: true |
| %n | Line Separator | Inserts a platformspecific line break. | String.format("Line 1%nLine 2") | Line 1 followed by Line 2 |
 */





/* Command shortcut:


javac Main.java
jar cfe Main.jar Main Main.class
java -jar Main.jar


 */