//
//  main.c
//  Triangle
//
//  Created by m garabedian on 4/9/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>




int main(int argc, const char * argv[])

{
    // declare a variable named 'totalTriangle' of type float
    float totalTriangle;
    
    // declare a variable named 'angleA' of type float
    float angleA;
    
    // declare a variable named 'angleB' of type float
    float angleB;
    
    // declare a variable named 'anglec' of type float
    float angleC;
    
    // store a value in that variable
    totalTriangle = 180;
    
    // the value attributed to angleA
    angleA = 30.0;
    
    // the value attributed to angleB
    angleB = 60.0;
    
    // the calculation of angleC by subtracting it from sum of angleA and angleB
    angleC = totalTriangle - (angleA + angleB);
    
    // the .2 in the printf line below limits output to two decimal points
    printf("The third angle is %.2f degrees. \n", angleC);
    return 0;
}
