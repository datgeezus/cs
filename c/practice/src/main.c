#include <stdio.h>

enum pset
{
    PSET_BRACKET_VALIDATOR = 29,
    PSET_MESH_MESSAGE = 46,
};

extern void pset__bracket_validator(void);
extern void pset__mesh_message(void);

int main()
{
    pset__bracket_validator();
    pset__mesh_message();
    getchar();
    return 0;
}