//
//  main.c
//  BeerSong
//
//  Created by m garabedian on 4/9/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>

void singSongFor(int numberOfBottles)
{
    if (numberOfBottles == 0) {
    printf("There are simply no more bottles of beer on the wall. \n\n");
    } else {
        printf("%d bottles of beer on the wall. %d bottles of beer. \n",
               numberOfBottles, numberOfBottles);
        int oneFewer = numberOfBottles - 1;
        printf("Take one down, pass it around, %d bottles of beer on the wall. \n\n", oneFewer);
        singSongFor(oneFewer); //This function calls itself!
        
        // Print a message just before the function ends
        printf("Put a bottle in the recycling, %d empty bottles in the bin. \n", numberOfBottles);
    }
}

int main(int argc, const char * argv[])
{
    // We could sing 99 verses, but 4 is easier to think about
    singSongFor(4);
    return 0;
}
