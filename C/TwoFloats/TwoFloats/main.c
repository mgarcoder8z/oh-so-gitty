//
//  main.c
//  TwoFloats
//
//  Created by m garabedian on 4/9/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    
    // Declare variable called 'firstNumber' of type float
    float firstNumber;
    
    // Store a number in that variable
    firstNumber = 3.14;
    
    // Log it to the user
    printf("The first Number is %f. \n", firstNumber);
    
    // Declare variable called 'secondNumber' of type float
    float secondNumber;
    
    // Store a number in that variable
    secondNumber = 14.0;
    
    // Log it to the user
    printf("The second Number is %f. \n", secondNumber);
    
    // Declare a variable called 'sumNumbers' of type float
    float sumNumbers;
    
    // Add the first and second numbers together
    sumNumbers = firstNumber + secondNumber;
    
    // Log that to the user
    printf("The sum of the first and second numbers is %f. \n", sumNumbers);
    
    // End this function and indicate success
    
    return 0;
}
