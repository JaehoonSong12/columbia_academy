/*
 * This program demonstrates how to read and use
 * "command-line arguments" passed to the main function.
 * Command Usages:
 *   1. gcc main.c -o candy
 *   2. ./candy 
 *   3. ./candy arg1 arg2 arg3
 *   4. rm -rf *.exe
 */
#include <stdio.h> // "ST"an"D"ard "I"nput "O"utput's (.) "H"eader
#include <stdlib.h> // "ST"an"D"ard "LIB"rary Required for malloc and free

// #include <cs50.h> // For get_string and get_int functions, CS50: Introduction to Computer Science, a popular introductory computer science course from Harvard University.
#include "cs50.h"

#include <ctype.h> // Required for toupper() and tolower() functions


int main(int argc, char** argv) {

    // Print the total number of arguments (program name + user args)
    // 'argc' stands for "argument count"
    printf("Total arguments passed: %d\n", argc);


    char input = 'A';
    switch (input) {
        case 'A':
        case 'a':
            printf("Hello Agent A!\n");
            break;
        case 'B':
        case 'b':
            printf("Hello Agent B!\n");
            break;
        default:
            printf("Hello Unknown Agent!\n");
            break;
    }


    while(1) {
        int x = get_int("Please enter the number of gummybear: ");
        int y = get_int("Please enter the number of lollipop: ");
        int z = get_int("Please enter the number of chocolate bar: ");
        if (x + 2*y + 0.7*z > 20){
            printf("Discount has been applied.\n");
            printf("total cost:%.2f\n", (x + 2*y + 0.7*z) * 0.9);
        } else {
            printf("Discount has not been applied.");
            printf("total cost:%.2f\n", (x + 2*y + 0.7*z));
        }

        char exit = toupper(get_char("Do you want to exit? (y/n): "));
        if (exit == 'Y') break;
    }



    /*
     우선 실행을 시키면, 저기 위에 코드대로 우선 사탕갯수를 입력하잖아요? 
     그러면 가격이 각각 나올텐데, 우선 구매자가 이 코드를 종료하기 전까지는 쇼핑을 계속 반복할수 있게 
     */ 





















    // Print the name of the program itself
    // This is always stored in argv[0]
    // 'argv' stands for "argument vector"
    printf("Program name: %s\n", argv[0]);
    printf("------------------------------\n");
    printf("Arguments received:\n");
    printf("index 1: %s\n", argv[1]);
    // printf("index 2: %s\n", argv[2]);
    // printf("index 3: %s\n", argv[3]);
    printf("------------------------------\n");
    for (int i = 1; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }

    // int i = 0;
    // while (i < 5) {
    //     printf("Hello %d\n", i);
    //     i = i+1;
    // }



    for(int i = 0; i < 5; i += 2){
        // even numbers only
        printf("Hello %d\n", i);
    }


    // for (int i = 0; i < 3; i++) {
    //     printf("arr[%d]: %d\n", i, arr[i]);
    // }

    // ./jihoo_python.exe main.py
    // [./jihoo_python.exe, main.py]
    // [./jihoo_python.exe, main.py, hi.py]
    // Array (Vector): [main.py, ..., hi.py]


    // [6, 1, -4] = 
    // 0th index: 6
    // 1st index: 1
    // 2nd index: -4
    // [argv[1], argv[2], argv[3]] = [6, 1, -4]
    // []


    





    int a = 10;
    int b = 5;
    int sum = a + b;
    printf("Sum: %d\n", sum);
    printf("Hello, C World!\n");
    printf("Let's look at our variables.\n");
    // wait input to exit (prompt needed)
    printf("Press Enter to exit..."); scanf("%*c");
    return 0;
}


// The gcc command is used for compiling C programs 
// because GCC, or the {GNU Compiler Collection}, 
// is the standard and widely used compiler for the 
// C programming language (among others like C++, Objective-C, Fortran, etc.).