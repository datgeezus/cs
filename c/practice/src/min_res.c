#include <limits.h>
#include <stdio.h>

static int findPair(int arr[], int N);

// Function to find a pair in an array with minimum absolute sum
static int findPair(int arr[], int N)
{
	if (N < 2)
	{
		return -1;
	}


	// maintain two indexes pointing to end-points of the array
	int low = 0;
	int high = N - 1;

	// min stores minimum absolute difference
	int min = INT_MAX;
	int i, j;

	// reduce search space arr[low..high] at each iteration of the loop

	// loop till low is less than high
	while (low != high)
	{
        int subs = (arr[high] - arr[low]) >= 0 ? (arr[high] - arr[low]) : (arr[low] - arr[high]);
		if (subs < min)
		{
			min = subs;
			i = low;
			j = high;
		}

		// optimization - pair with 0 sum is found
		if (min == 0)
			break;

		// increment low index if total is less than 0
		// decrement high index is total is more than 0
		(subs > 0)? low++: high--;
	}

    return arr[i] - arr[j];

}

// Find Pair in an Array having Minimum Absolute Sum
int main()
{
	int arr[] = { 8, 24, 3, 20, 1, 17 };
	int n = sizeof(arr)/sizeof(arr[0]);

	printf("min: %d \n", findPair(arr, n));

	return 0;
}