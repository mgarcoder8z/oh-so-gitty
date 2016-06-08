//
//  main.c
//  Countdown
//
//  Created by m garabedian on 4/13/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[])

{
    // counts down from 99 by threes
    int i;
    
    for (i = 99; i > 0; i -= 3) {
        printf("%d. \n", i);
        if (i % 5 == 0) {
            printf("I found one \n");
        }
    }
    
    // the -= is shorthand for subtract by that number 3
    
    

   {
        while (i > 0)
        {
        printf("Reached zero no negatives %d.\n", i);
        i -= 3;
        break;
        }
    }
    
    return 0;
}
