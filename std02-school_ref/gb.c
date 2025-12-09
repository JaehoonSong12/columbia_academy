#include <stdio.h>

struct Gb{
    int x;
    int y;
    string positionPrompt;
    string secondaryPrompt;
};

struct Gb createGb(int x, int y, string positionPrompt, string secondaryPrompt)
{
    struct Gb gb;
    gb.x = x;
    gb.y = y;
    gb.positionPrompt = positionPrompt;
    gb.secondaryPrompt = secondaryPrompt;
    return gb;
}