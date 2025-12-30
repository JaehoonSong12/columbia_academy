#include <stdio.h>
#include <stdarg.h>         // for va_list, va_start, va_end, vsnprintf
#include "cs50.h"
#include <stdlib.h>

int rand_range(int min, int max) {
    return min + rand() % (max - min + 1);
}







int main(int argc, char* argv[]) {
    printf("---------Project for Python Library---------: %s\n", argv[0]);
    for (int i = 1; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    printf("------------------------------\n");
}









// floating number addition, subtraction, multiplication, division calculator, data type defined for python binding
float add(float a, float b) {
    return a + b;
}

void intro_message(void) {
    printf("This is a simple calculator for addition, subtraction, multiplication, and division of floating point numbers.\n");
}

void quiz_time(void) {
    // 1. ask user to input an integer
    // 2. the user should guess what the integer is.
    // 3. if the user guesses correctly, print "Correct!"
    // 4. if the user guesses incorrectly, print either "Too high!" or "Too low!" accordingly.
    int answer = rand_range(1, 100);
    while (1) {
        int user_input = get_int("Please enter your number: ");
        printf("You entered: %d\n", user_input);
        if (user_input == answer) {
            printf("You are right!\nbb\n");
            break;
        } else if (user_input < answer){
            printf("Your number is smaller than answer\n");
        } else if (user_input > answer){
            printf("Your number is bigger than answer\n");
        }
    }
}