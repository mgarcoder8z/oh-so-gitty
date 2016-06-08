//
//  main.c
//  Squarer
//
//  Created by m garabedian on 4/10/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>

// define a variable called 'numbertosquare' of type int
int numbertosquare;

// define a variable called 'squared' of type int
int squared;


int main(int argc, const char * argv[]) {
    
    numbertosquare = 5;
    squared = (numbertosquare * numbertosquare);
    printf("\"%d\" squared is \"%d.\" \n", numbertosquare,squared);
    return 0;
}
