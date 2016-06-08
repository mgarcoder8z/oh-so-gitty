//
//  main.c
//  CountdownUserInput
//
//  Created by m garabedian on 4/13/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>
#import <readline/readline.h>

int main(int argc, const char * argv[]) {
    
        // counts down from 99 by threes and prints the number
        int i;
    
        // the -= is shorthand for subtract by that number, or three less in this case
        
        for (i = 99; i > 0; i -= 3) {
            printf("%d. \n", i);
            
        // if multiples of 5 are found, print I found one, the double == means equal to
            if (i % 5 == 0) {
                printf("I found one \n");
            }
        }
        
        {
        // while i is greater than zero it prints numbers and then breaks
            while (i > 0)
            {
                printf("Reached zero no negatives %d.\n", i);
                i -= 3;
                break;
            }
        }
        
        return 0;
    }
