#include<iostream>
// OOP library to use your default input-output system (mouse, monitor, keyboard...)


/*
 * rm -rf build/                        - clean
 * cmake -S . -B build                  - build (providing os-specific 'make' script)       CMake -> make
 * cmake --build build -j$(nproc)       - build (proxy to run 'make' command)               make -> .exe
 * 
 */



#include<stdio.h>
// procedural library to use your default input-output system (mouse, monitor, keyboard...)

// void * printf (.....) {
//     /////
// }












 /*
 rm -rf build/
 cmake -S . -B build
 cmake --build build -j$(nproc)
 ./build/music_app.exe
 */


void c_example(); // function prototype (proxy of implementation, declaration)
// defines a pointer (value of memory address), so complier recognizes some "value".

void cpp_example();


int main() {

    // c_example();
    cpp_example();
    return 0; // error thrown, signal of failure.
}


void c_example() { // actual implementation, definition
    char * str = 0;
    printf("Hi there\n"); // C code, runnable on C++


    printf("Your program is running, enter any greetings you want! : "); // C code, runnable on C++
    scanf("%s", str);

    printf("You entered: %s", str);



    printf("Your program is running, enter any keys to close this window... "); 
    scanf("%s", str);
    return;
}

// make a PR please!
void cpp_example() {
    std::string s;

    std::cout << "Hi there" << std::endl;
    std::cout << "Enter any greetings you want: ";

    std::getline(std::cin, s);

    std::cout << "You entered: " << s << std::endl;

    std::cout << "Press Enter to close this window...";
    std::cin.get();
}




// 404 Error: Page not found
