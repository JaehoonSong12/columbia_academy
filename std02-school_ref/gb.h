// gb.h
#ifndef GB_H // GB stands for "Game Board"
#define GB_H

#include "cs50.h" // Required so 'string' is recognized inside the struct



typedef char* string;
typedef struct gb {
    int x;
    int y;
    string positionPrompt;
    string secondaryPrompt;
    bool isWall;
} gb;

// Prototype only (no code body)
struct gb createGb(int x, int y, string positionPrompt, string secondaryPrompt);
struct gb createGbWall(int x, int y, string positionPrompt, string secondaryPrompt);


#endif