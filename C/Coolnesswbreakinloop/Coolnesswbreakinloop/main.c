//
//  main.c
//  Coolnesswbreakinloop
//
//  Created by m garabedian on 4/13/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[])

{
    int i;
    for (i = 0; i < 12; i++) {
        
        // tells program to continue and jump forward if multiples of three found
        if (i % 3 == 0) {
            continue;
        }
        // executes the block until answer is found, skipping multiples of 3
        printf("Checking i = %d\n", i);
               if (i + 90 == i * i) {
                   break;
            }
        }
        //prints out answer, having skipped multiples of three like 3, 6 and 9
               printf("The answer is %d.\n", i);
               return 0;
}