//
//  main.c
//  Coolness
//
//  Created by m garabedian on 4/13/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    
    // start with integer of zero
    int i = 0;
    
    // while integer is less than twelve
    while (i < 12) {
        
        // print Aaron is cool up to twelve times
        printf("Aaron is cool\n");
        
        //increment the integer by one each time of loop returns false, otherwise infinite loop occurs
        i++;
    }
    return 0;
}
