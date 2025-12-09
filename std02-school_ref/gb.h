// gb.h
#ifndef GB_H // GB stands for "Game Board"
#define GB_H

#include "cs50.h" // Required so 'string' is recognized inside the struct

struct Gb {
    int x;
    int y;
    string positionPrompt;
    string secondaryPrompt;
    int isWall;
};

// Prototype only (no code body)
struct Gb createGb(int x, int y, string positionPrompt, string secondaryPrompt);
struct Gb createGbWall(int x, int y, string positionPrompt, string secondaryPrompt);

#endif