//
//  main.c
//  TurkeyTimer
//
//  Created by m garabedian on 4/9/16.
//  Copyright © 2016 Big Nerd Ranch. All rights reserved.
//

#include <stdio.h>

void showCookTimeForTurkey(int pounds)
{
    int necessaryMinutes = 15 + 15 * pounds;
    printf("Cook for %d minutes. \n", necessaryMinutes);
    if (necessaryMinutes>120) {
        int halfway = necessaryMinutes / 2;
        printf("Rotate after %d of the %d minutes. \n", halfway, necessaryMinutes);
    }
}

int main(int argc, const char * argv[]) {
    int totalWeight = 10;
    int gibletsWeight = 1;
    int turkeyWeight = totalWeight - gibletsWeight;
    showCookTimeForTurkey(turkeyWeight);
    
    return 0;
}
