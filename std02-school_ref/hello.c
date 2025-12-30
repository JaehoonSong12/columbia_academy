/*
 * This program demonstrates how to read and use
 * "command-line arguments" passed to the main function.
 * Command Usages:
 *   1. gcc main.c -o candy
 *   2. ./candy 
 *   3. ./candy arg1 arg2 arg3
 *   4. rm -rf *.exe
 */



// Jihoo Choi
// 25 Nov 14
// 2nd period IST
#include <stdio.h>
#include <string.h>

#include "cs50.h"
#include "gb.h"


__declspec(dllexport) int runApp(void) {
    struct gb darkenCave[32][33];

    for(int i = 0; i < 32; i++)
    {
        for (int j = 0; j < 33; j++)
        {
            darkenCave[i][j] = createGb(i, j, "You are in darken cave.", "There's nothing special, but you feel like something looking at you. You are holding a torch turned off the light.");
        }
    }
    //special position for event
    darkenCave[12][31] = createGb(12,31, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][30] = createGb(12,30, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][29] = createGb(12,29, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][28] = createGb(12,28, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Turch is turned off");
    darkenCave[12][27] = createGb(12,27, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][26] = createGb(12,26, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][25] = createGb(12,25, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][24] = createGb(12,24, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[1][24] = createGb(1,24, "You are in darken cave.", "There is a ladder you have climbed.");
    darkenCave[4][27] = createGb(4,27, "You are in darken cave.", "There is a spider alert.");
    darkenCave[7][27] = createGb(4,27, "You are in darken cave.", "The spider owner is looking at you.");
    //making the wall
    darkenCave[0][23] = createGbWall(0,23, "You are in dark Cave", "This is a wall.");
    darkenCave[1][23] = createGbWall(1,23, "You are in dark Cave", "This is a wall.");
    darkenCave[2][23] = createGbWall(2,23, "You are in dark Cave", "This is a wall.");
    darkenCave[3][23] = createGbWall(3,23, "You are in dark Cave", "This is a wall.");
    darkenCave[4][23] = createGbWall(4,23, "You are in dark Cave", "This is a wall.");
    darkenCave[5][23] = createGbWall(5,23, "You are in dark Cave", "This is a wall.");
    darkenCave[6][23] = createGbWall(6,23, "You are in dark Cave", "This is a wall.");
    darkenCave[7][23] = createGbWall(7,23, "You are in dark Cave", "This is a wall.");
    darkenCave[8][23] = createGbWall(8,23, "You are in dark Cave", "This is a wall.");
    darkenCave[9][23] = createGbWall(9,23, "You are in dark Cave", "This is a wall.");
    darkenCave[10][23] = createGbWall(10,23, "You are in dark Cave", "This is a wall.");
    darkenCave[11][23] = createGbWall(11,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][23] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][22] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][21] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][20] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][19] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][18] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][17] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][16] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][15] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][14] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][13] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][12] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][11] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][10] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[12][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[13][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[14][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[15][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[16][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[17][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[18][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[19][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[20][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[21][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[22][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[23][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[24][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[25][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[26][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[27][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[28][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[29][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[30][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");
    darkenCave[31][9] = createGbWall(12,23, "You are in dark Cave", "This is a wall.");


    //define player position
    int playerX = 0;
    int playerY = 24;
    bool gameRunning = true;
    char command;
    //game loop
    while(gameRunning)
    {
        //basic notification for position and situation
        printf("Player position:(%d,%d)\n", playerX, playerY);
        printf("%s\n", darkenCave[playerX][playerY].positionPrompt);
        printf("%s\n", darkenCave[playerX][playerY].secondaryPrompt);
        if (playerX == 13){
            printf("You are likely to be eaten by \'Lighty\' beacuse of the darkness of torch.\n");
        }
        //Enter Prompt
        printf("Enter command (e/w/s/n) to move, q to quit: ");
        command = getchar();
        getchar();
        //initializing player walking Prompt
        switch (command)
        {
            case 'n':
                if (playerY < 33){
                    if (darkenCave[playerX][playerY + 1].isWall){
                        printf("You can't proceed to this direction.\n");
                    } else {playerY++;}
                }
                break;
            case 's':
                if (playerY > 0){
                    if (darkenCave[playerX][playerY - 1].isWall){
                        printf("You can't proceed to this direction.\n");
                    } else {playerY--;}
                }
                break;
            case 'e':
                if (playerX < 32){
                    if (darkenCave[playerX + 1][playerY].isWall){
                        printf("You can't proceed to this direction.\n");
                    } else {playerX++;}
                }
                break;
            case 'w':
                if (playerX > 0){
                    if (darkenCave[playerX - 1][playerY].isWall){
                        printf("You can't proceed to this direction.\n");
                    } else {playerX--;}
                }
                break;
        //game quiting and invalid Prompt
            case 'q':
                gameRunning = false;
                printf("Thanks for playing!\n");
                break;
            default:
                printf("Invalid command, please try again.\n");
                break;

        }
    }




    return 0;
}



int main(int argc, char *argv[]) {
    printf("---------Program name---------: %s\n", argv[0]);
    for (int i = 1; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    printf("------------------------------\n");


    runApp();

    return 0;
}





 
// // Jihoo Choi
// // 25 Nov 14
// // 2nd period IST
// #include <stdio.h>
// #include <string.h>
// #include <stdlib.h>
// #include <stdbool.h>


// #include "cs50.h"
// #include "gb.h"




// int main(int argc, char *argv[])
// {
//     printf("---------Program name---------: %s\n", argv[0]);
//     for (int i = 1; i < argc; i++) {
//         printf("Argument %d: %s\n", i, argv[i]);
//     }
//     printf("------------------------------\n");




//     int width = 23;
//     int height = 33;
//     struct Gb darkenCave[width][height]; // hardcoding, avoid it.
//     for(int i = 0; i < width; i++) {
//         for (int j = 0; j < height; j++) {
//             darkenCave[i][j] = createGb(
//                 i, j, 
//                 "You are in darken cave.", 
//                 "There's nothing special, but you feel like something looking at you. You are holding a torch turned off the light."
//             );
//         }
//     }
//     darkenCave[13][31]  = createGb(13, 31,  "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
//     darkenCave[13][30]  = createGb(13, 30,  "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
//     darkenCave[13][29]  = createGb(13, 29,  "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
//     darkenCave[13][28]  = createGb(13, 28,  "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Turch is turned off");
//     darkenCave[13][27]  = createGb(13, 27,  "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
//     darkenCave[13][26]  = createGb(13, 26,  "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
//     darkenCave[13][25]  = createGb(13, 25,  "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
//     darkenCave[13][24]  = createGb(13, 24,  "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
//     darkenCave[1][24]   = createGb(1,  24,  "You are in darken cave.", "There is a ladder you have climbed.");
//     darkenCave[4][27]   = createGb(4,  27,  "You are in darken cave.", "There is a spider alert.");
//     darkenCave[7][27]   = createGb(7,  27,  "You are in darken cave.", "The spider owner is looking at you.");

//     darkenCave[0][23]   = createGbWall(0,23,"You are in darken cave.", "You hit a wall.");

//     //initialize
//     int playerX = 0;
//     int playerY = 24;
//     bool gameRunning = true;
//     // bool turningTorch = false;
//     char command;

//     while(gameRunning) {
//         // player status display
//         printf("Player position:(%d,%d)\n", playerX, playerY);
//         printf("%s\n", darkenCave[playerX][playerY].positionPrompt);
//         printf("%s\n", darkenCave[playerX][playerY].secondaryPrompt);
//         // game logic
//         if (playerX == 13) printf("You are likely to be eaten by \'Lighty\' beacuse of the darkness of torch.\n");


//         printf("Enter command (e/w/s/n) to move, q to quit: ");
//         command = getchar();
//         getchar();

//         switch (command) {
//             case 'n':
//                 if (playerY < height) {
//                     if (darkenCave[playerX][playerY + 1].isWall) printf("You can't go through the wall.\n");
//                     else playerY++;
//                 }
//                 else printf("You can't go further north.\n");
//                 break;
//             case 's':
//                 if (playerY > 0) {
//                     if (darkenCave[playerX][playerY - 1].isWall) printf("You can't go through the wall.\n");
//                     else playerY--;
//                 }
//                 else printf("You can't go further south.\n");
//                 break;
//             case 'e':
//                 if (playerX < width) {
//                     if (darkenCave[playerX + 1][playerY].isWall) printf("You can't go through the wall.\n");
//                     else playerX++;
//                 }
//                 else printf("You can't go further east.\n");
//                 break;
//             case 'w':
//                 if (playerX > 0) {
//                     if (darkenCave[playerX - 1][playerY].isWall) printf("You can't go through the wall.\n");
//                     else playerX--;
//                 }
//                 else printf("You can't go further west.\n");
//                 break;
//             case 'q':
//                 gameRunning = false;
//                 printf("Thanks for playing!\n");
//                 break;
//             default:
//                 printf("Invalid command, please try again.\n");
//                 break;
//         }
//     }




//     return 0;
// }