#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "cs50.h"




















void askString() {
    while (1) {
        char* str = get_string("Input a string: (empty to quit) ");
        if (str == NULL || strlen(str) == 0){
            free(str);
            break;
        }
        printf("You entered: %s\n", str);
        free(str);
        // make: *** [makefile:19: run] Error -1073740940
    }
    return;
}





int main(int argc, char* argv[]){
    for (int i = 0; i < argc; i++){
        printf("Argument %d: %s\n", i, argv[i]);
    }

    int x = 42;
    printf("The answer is %d\n", x);
    printf("The address of x is %p\n", (void*)&x);


    int* pointer = &x;
    printf("The value at pointer is %d\n", *pointer);
    printf("The address stored in pointer is %p\n", (void*)pointer);


    // array example
    int numbers[3] = {10, 20, 30};
    printf("The address of numbers is %p\n", (void*)numbers);
    for (int i = 0; i < 3; i++){
        printf("numbers[%d] = %d\n", i, numbers[i]);
        printf("numbers[%d] = %d\n", i, *(numbers + sizeof(int) * i));
    }

    // malloc example ("m"emory "alloc"ation)
    int* array = malloc(5 * sizeof(int));
    printf("The size of integer data type is %lld bytes\n", sizeof(int));
    printf("The address of array is %p\n", (void*)array);
    for (int i = 0; i < 5; i++){
        array[i] = i * i;
        printf("array[%d] = %d\n", i, array[i]);
    }
    free(array);

    // char* str = {'H','e','l','l','o','\0'};
    // printf("String: %s\n", str);

    askString();
    askString();
    askString();
    
    
    // int arr[4] = {1,2,3,4};
    // printf("Hello, World!\n");
    return 0;
}