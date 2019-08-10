#include <stdio.h>
#include <stdlib.h>


/*
    In a microcontroller-based system, analogue to digital converter (ADC) is sensing analogue voltage coming on one of the analogue channels.
    This analogue voltage needs to be converted into a discrete level (0-4) depending upon the value of input voltage in such a way that some hysteresis
    is added to reject sudden voltage variations due to noise. Following graph shows the relationship between analogue voltage read (%age) from the channel
    to the discrete level that need to be encoded by the software. Write code that will perform this job.
    [Hint 1: If analogue voltage increases from 5% to 16% encoded step shall be 1 and if it decreases back to 11% from 16%, the encoded level shall remain 1 unless voltage drops to 10%.
    Hint 2: use this prototype so the code can be tested: unsigned int hysteresis(unsigned int input_percent)]
 */

static unsigned int hysteresis(unsigned int input_percent);

int main()
{
    unsigned int test[] = { 0, 5, 16, 11, 10, 100, 86, 70, 86, 22};

    int i = 1;
    for(; i < 10; ++i)
    {
        printf("from: %d to:%d  hyst: %d \n", test[i-1],  test[i], hysteresis(test[i]));
    }

    /* Test outputs:
     * from: 0 to:5  hyst: 0 
     * from: 5 to:16  hyst: 1 
     * from: 16 to:11  hyst: 1 
     * from: 11 to:10  hyst: 0 
     * from: 10 to:100  hyst: 4 
     * from: 100 to:86  hyst: 4 
     * from: 86 to:70  hyst: 3 
     * from: 70 to:86  hyst: 3 
     * from: 86 to:22  hyst: 1 
     */

    getchar();
    return 0;
}

static unsigned int hysteresis(unsigned int input_percent)
{
    static unsigned int level = 0; /* stores and remembers last level */
    unsigned int ranges[5][2] =
        {
            {0, 10},
            {15, 35},
            {40, 60},
            {65, 85},
            {90, 100},
        };

    int i = 0;
    for (; i < 5; ++i)
    {
        /* check if the input_percent is in a valid range */
        if ((input_percent >= ranges[i][0]) &&
            (input_percent <= ranges[i][1]))
        {
            level = i;
        }
    }

    /* if the input_percent is not in the ranges it will take the last level */

    return level;
}