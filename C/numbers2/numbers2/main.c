//
//  main.c
//  numbers2
//
//  Created by m garabedian on 4/12/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>

//stdlib includes decimal and scientific 'e' data type
#include <stdlib.h>

// math.h includes math libraries
#include <math.h>

int main(int argc, const char * argv[]) {
    double y = 12345.6789;
    //printf below for f is regular decimal limited to two decimal places with the .2
    printf("y is %.2f\n", y);
    
    //print f below for e is for scientific number format limited to two decimal places with .2
    printf("y is %.2e\n", y);
    return 0;
}
