// gb.c
#include <stdio.h>
#include "gb.h" // Includes the struct definition and cs50.h

struct gb createGb(int x, int y, string positionPrompt, string secondaryPrompt)
{   gb a;
    a.x = x;
    a.y = y;
    a.positionPrompt = positionPrompt;
    a.secondaryPrompt = secondaryPrompt;
    a.isWall = false;
    return a;
}

struct gb createGbWall(int x, int y, string positionPrompt, string secondaryPrompt)
{   gb a;
    a.x = x;
    a.y = y;
    a.positionPrompt = positionPrompt;
    a.secondaryPrompt = secondaryPrompt;
    a.isWall = true;
    return a;
}
