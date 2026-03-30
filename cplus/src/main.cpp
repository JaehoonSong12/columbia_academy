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














void c_example(); // function prototype (proxy of implementation, declaration)
// defines a pointer (value of memory address), so complier recognizes some "value".

void cpp_example();







double multiply(double x, double y) {
    return x * y;
}


// double multiply(double * x, double y) {
//     return x * y;
// }


// int pointerPractice(int * x) { // mem#2: 0x_address
//     *(x) = 20;
//     return 0;
// }

namespace Scalar {
    double multiply(double * vec1, double * vec2) { // Scalar::multiply
        double product = 0;
        for(int i = 0; i < 3; i++) {
            product += vec1[i] * vec2[i];
        }
        return product;
    }
}

namespace Vector {
    double * multiply(double * vec1, double * vec2) { // Vector::multiply
        double * product = new double[3];
        product[0] =   vec1[1] * vec2[2] - vec1[2] * vec2[1];
        product[1] = -(vec1[0] * vec2[2] - vec1[2] * vec2[0]);
        product[2] =   vec1[0] * vec2[1] - vec1[1] * vec2[0];
        return product;
    }
}





int main() {
    // c_example();
    // cpp_example();


    std::cout << multiply(5, 8) << std::endl;

    // CPP concept #1: pointer (reference - same size as integer) + array
    // int x = 10;                                // mem#1: 10
    // std::cout << x << std::endl; // 10

    // pointerPractice(&x);
    // std::cout << x << std::endl; // 


    double vec1[3] = {1,2,3};
    double vec2[3] = {4,2,1};
    // multi-varaible, scalar product (dot product) & vector product (cross product)
    std::cout << "dot product of vec1 and 2: " << Scalar::multiply(vec1, vec2) << std::endl;
    double * vec3 = Vector::multiply(vec1, vec2);
    std::cout << "cross product of vec1 and 2: ";
    for (int i = 0; i < 3; i++) {
        std::cout << vec3[i] << ",";
    }

    // PR please! :) ok




    // char * ptr;
    // float * ptr;
    // ptr = &x;

    
    // std::cout << "How to get Addresses!!!" << std::endl;
    // std::cout << ptr << std::endl;
    // std::cout << &ptr << std::endl;

    // std::cout << &x << std::endl;

    
    // std::cout << "How to get the Values!!!" << std::endl;
    // std::cout << *(ptr) << std::endl; // dereference operator (unary)

    // *(ptr) = 15;



    return 0; // error thrown, signal of failure.
}
/*
rm -rf build/
cmake -S . -B build
cmake --build build -j$(nproc)
./build/music_app.exe
*/







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



// Programming Paradigms

// 1. Procedural (functions + machine's data)

// 2. Object-Oriented (encapsulated objects, each has its own state.)
// Class obj = new ....
// obj.setProperty(...) // mutable state

// 3. Functional programming (lambda programming, basic idea SAM, Single Abstract Method class)
// lambda binary_summation = (a,b) -> { return a + b } /// immutable state


// 404 Error: Page not found
