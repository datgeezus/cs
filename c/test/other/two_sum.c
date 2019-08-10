
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>


/* Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
 */

static int nums[] = {2, 7, 11, 15};
static int target = 9;

int main()
{
    int size = -1;
    int *values = twoSum(nums, 4, target, &size);
    getchar();
    return 0;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    uint64_t mem = 0;
    int i = 0;
}
