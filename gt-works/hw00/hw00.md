# Java Basics

## Problem Description
Hello, and welcome to your first homework assignment! Do not worry though – this assignment is not graded. This assignment just serves to make sure you have installed Java properly on your machine and that you know how to run a Java program.  

---

## Part One: Installing Java

In this class, we will be using Java 11 (OpenJDK, Zulu distribution by Azul). Make sure you have this version installed, even if you already have a previous version of Java. We have detailed instructions for this here: **Installing Java Guide (JDK 11).pdf**

Check to see which version of Java you have installed by running `javac --version` and `java --version`.

After running `javac --version`, you should see something like this output (your version number might be greater, e.g. 11.0.18):

```
javac 11.0.17
```

After running `java --version`, you should see something like this output:

```
openjdk 11.0.17 2022-10-18 LTS
OpenJDK Runtime Environment Zulu11.60+19-CA (build 11.0.17+8-LTS)
OpenJDK 64-Bit Server VM Zulu11.60+19-CA (build 11.0.17+8-LTS, mixed mode)
```

---

## Part Two: Writing and Compiling a Java Class

In order to create a Java class, you must first create a file with the `.java` extension. In our example here, we will use `Test.java`. Within the class, you will need to write a class header. For now, just memorize that you need to write `public class` before your class name. We will go more in-depth about what exactly this means later. As for the class name, it must exactly match the name of the file.

Thus, our example should look like this:

```java
public class Test {

}
```

Now that you have written a Java class, you should be able to compile your code. Navigate to the directory where you have saved this file in the command line. After navigating to the proper directory, you will be able to compile the Java class you just created! You do this by using the command:

```
javac FileName.java
```

Since we named our Java example file `Test.java`, we compile it using:

```
javac Test.java
```

This should create a new file in your directory called `Test.class`! This file is created by the Java compiler and contains Java bytecode. If you open it up, the contents will not make much sense to you. However, it makes a lot of sense to the Java Virtual Machine, or the JVM (a computing machine that allows our program to run). 

If a new file was not created, your program did not compile. Read the compilation error produced in your command prompt, and fix it before proceeding!

---

## Part Three: The `main` Method

In Java, we need the following method for our class to run. Unlike, say, Python, if the JVM does not see this method, it cannot execute the program!

```java
public static void main(String[] args) {

}
```

Write a `main` method for your `Test` class. All the code you wish to run will be written inside of your `main` method!

Now, you can write the contents of your first Java program! Let's start by printing out a message using the method `System.out.println()`. Refer back to the first module’s content on Canvas if you get stuck.

To run your program, use the command:

```
java FileName
```

Since we named our file `Test.java`, we will use the command:

```
java Test
```

Note that we didn’t include the `.class` extension after `Test`; it won’t run if you do `java Test.class`. If you ever want to run a new version of your program after making alterations, know that you must recompile before doing so.

Good luck, and happy hacking!

---

## Part Four: JavaFX Verification and Submission

At the end of the course, we will use JavaFX to create a GUI. To avoid some compatibility issues, we need to verify that your installation can properly compile and run Java classes that use JavaFX. Follow these steps:

1. **Download and compile JavaFXCheck.java**  
   Download `JavaFXCheck.java`. Note that you don't need to understand the code in this file.

2. **Run the program**, which will prompt you to enter your name in the console (type and hit return/enter) and then show a GUI.

3. **Check if the screenshot** has the same Java and JavaFX versions as the one in the image below. Check if the OS information matches the one from your PC / Mac (can be different from image) and that the name is your full name.

4. If it does, **take a screenshot** (convert it to `.png` if it isn't in that format), and name it `javafx-screenshot.png`.

5. **Submit the `.png` file in Gradescope**, in the HW0 assignment.

`Screen Shot 2023-01-08 at 2.43.11 PM.png`

---

## Closing Comments

If you had trouble with any parts of this homework, reach out to your TAs! You can reach us through office hours, email, and Piazza. Feel free to also bring any questions to recitation. We would love to help you figure out the basics before jumping into Homework 1. The TAs are here to help you succeed in this course!
