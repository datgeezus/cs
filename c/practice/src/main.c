#include <stdio.h>

enum pset
{
    PSET_BRACKET_VALIDATOR = 29,
    PSET_MESH_MESSAGE = 46,
};

extern void pset__bracket_validator(void);
extern void pset__mesh_message(void);
extern void pset_balanced_binary_tree();
extern void pset_cake_thief();
extern void number_of_islands();
extern void shortest_path_in_maze();

int main()
{
    printf("\npset__bracket_validator ...\n");
    // pset__bracket_validator();
    printf("\npset__mesh_message ...\n");
    // pset__mesh_message();
    printf("\npset_balanced_binary_tree ...\n");
    // pset_balanced_binary_tree();
    printf("\npset_caake_thief ...\n");
    // pset_cake_thief();
    printf("\npnumber_of_islands ...\n");
     number_of_islands();
    //shortest_path_in_maze();
    getchar();
    return 0;
}