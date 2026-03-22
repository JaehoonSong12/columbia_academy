// 
#include <stdio.h> // STanDard Input-Output

#include "cs50.h" // CS50 Library


// 
int main() {
    printf("Hello, World!!!!!!!!!!\n");

    char* name; // Array to store name

    // // show the address of name
    // printf("Address of name: %p\n", (void*)name);


    // printf("Done \n");

    // using cs50, get string input
    name = get_string("Enter your name: ");
    printf("Hello, %s!\n", name);

    // getchar(); // Wait for user input before closing
    return 0;
}



// 