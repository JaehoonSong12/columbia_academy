// gb.c
#include <stdio.h>
#include "gb.h" // Includes the struct definition and cs50.h

// The actual code for the function
struct Gb createGb(int x, int y, string positionPrompt, string secondaryPrompt) {
    struct Gb gb;
    gb.x = x;
    gb.y = y;
    gb.positionPrompt = positionPrompt;
    gb.secondaryPrompt = secondaryPrompt;
    gb.isWall = 0; // Default value for isWall
    return gb;
}


struct Gb createGbWall(int x, int y, string positionPrompt, string secondaryPrompt) {
    struct Gb gb;
    gb.x = x;
    gb.y = y;
    gb.positionPrompt = positionPrompt;
    gb.secondaryPrompt = secondaryPrompt;
    gb.isWall = 1;
    return gb;
}