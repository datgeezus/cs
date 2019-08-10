/* 

You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden. The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system. The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.

Given a list of non-negative integers nums representing the amount of money hidden in each house, determine the maximum amount of money you can rob in one night without triggering an alarm.

Example

For nums = [1, 1, 1], the output should be
houseRobber(nums) = 2.

The optimal way to get the most money in one night is to rob the first and the third houses for a total of 2.

 */

#include<stdio.h>
#include<stdlib.h>

#define MAX(a,b) (((a) >= (b)) ? (a) : (b))

static int test[] = { 1, 2, 3, 1 };

static int rob(int *nums, int numSize);

int main()
{
    printf("%d \n", rob(test, 4));
    getchar();
    return 0;
}


static int rob(int* nums, int numsSize){
    if(numsSize == 0)
    {
        return 0;
    }
    
    if(numsSize == 1)
    {
        return nums[0];
    }
    
    if(numsSize == 2)
    {
        return MAX(nums[0], nums[1]);
    }
    
    int mem[2];
    mem[0] = nums[0];
    mem[1] = MAX(nums[0], nums[1]);
    
    int i = 2;
    for(; i < numsSize; ++i)
    {
        int curr = MAX(mem[1], (nums[i] + mem[0]));
        mem[0] = mem[1];
        mem[1] = curr;
    }
    return mem[1] ;
}