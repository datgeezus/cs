#include <stdio.h>

enum pset
{
    PSET_BRACKET_VALIDATOR,
};

extern void pset__bracket_validator(void);

int main()
{
    pset__bracket_validator();
    getchar();
    return 0;
}