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
#include "gb.c"

int main(int argc, char *argv[])
{

    struct Gb darkenCave[33][23];

    for(int i = 0; i < 33; i++)
    {
        for (int j = 0; j < 23; j++)
        {
            darkenCave[i][j] = createGb(i, j, "You are in darken cave.", "There's nothing special, but you feel like something looking at you. You are holding a torch turned off the light.");
        }
    }
    darkenCave[12][7] = createGb(12,7, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][6] = createGb(12,6, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][5] = createGb(12,5, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][4] = createGb(12,4, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Turch is turned off");
    darkenCave[12][3] = createGb(12,3, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][2] = createGb(12,2, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][1] = createGb(12,1, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[12][0] = createGb(12,0, "You are in darken cave.", "Since this point, you are supposed to turn on the torch to go more east. Torch is turned off");
    darkenCave[1][0] = createGb(1,0, "You are in darken cave.", "There is a ladder you have climbed.");
    darkenCave[4][3] = createGb(4,3, "You are in darken cave.", "There is a spider alert.");
    darkenCave[7][3] = createGb(4,3, "You are in darken cave.", "The spider owner is looking at you.");


    //initialize
    int playerX = 0;
    int playerY = 0;
    bool gameRunning = true;
    bool turningTorch = false;
    char command;

    while(gameRunning)
    {
        printf("Player position:(%d,%d)\n", playerX, playerY);
        printf("%s\n", darkenCave[playerX][playerY].positionPrompt);
        printf("%s\n", darkenCave[playerX][playerY].secondaryPrompt);
        if (playerX > 12){
            printf("You are likely to be eaten by \'Lighty\' beacuse of the darkness of torch.\n");
        }
        printf("Enter command (e/w/s/n) to move, q to quit: ");
        command = getchar();
        getchar();

        switch (command)
        {
            case 'n':
                if (playerY < 8) playerY++;
                break;
            case 's':
                if (playerY > -15) playerY--;
                break;
            case 'e':
                if (playerX < 23) playerX++;
                break;
            case 'w':
                if (playerX > -1) playerX--;
                break;
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







