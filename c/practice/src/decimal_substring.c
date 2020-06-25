#include <stdio.h>

static int test[][2] = {
    { 10, 10},
    { 53, 1953786},
    { 53, 1953}

};

static int solution(int A, int B);

int main()
{
    int i = 0;
    for(; i < 3; ++i)
    {
        printf("pos:%d\n", solution(test[i][0], test[i][1]));
    }
}

static int solution(int A, int B)
{
    int i = 0;
    int ans = -1;
    for(; B > 0; ++i)
    {
        int and = A & B;
        printf("%d AND %d: %d\n", A, B, and);
        if(and == A)
        {
            ans = i;
        }
        B /= 10;
    }

    return A & B;
}
