#include <stdio.h>
#include <string.h>
#include "stack/stack.h"

const char *tests[] =
{
    "[]",
    "[{]",
    "[(sadasd{})]",
    "{{[[(())]]}}",
    "",
};

static int isValid(const char *code);
static int isOpener(const char c);
static int isCloser(const char c);
static char openerToCloser(const char c);

void pset__bracket_validator(void)
{
    int i = 0;

    for (i = 0; i < 5; ++i)
    {
        printf("Test %i: %s : %s\n", i, tests[i], isValid(tests[i]) == 1 ? "TRUE" : "FALSE");
    }
}

static int isValid(const char *code)
{
    int isValid = 1;
    size_t i = 0;
    size_t codeLen = strlen(code);
    Stack *openStack = Stack_New();

    for (i = 0; i < codeLen; ++i)
    {
        if (isOpener(code[i]))
        {
            Stack_PushChar(openStack, code[i]);
        }
        else if (isCloser(code[i]))
        {
            if (Stack_IsEmpty(openStack))
            {
                isValid = 0;
                break;
            }
            else
            {
                char test = Stack_PopChar(openStack);
                if (openerToCloser(test) == code[i])
                {
                    isValid = 1;
                }
                else
                {
                    isValid = 0;
                    break;
                }
            }
        }
    }

    return isValid;
}

static int isOpener(const char c)
{
    return c == '['
        || c == '{'
        || c == '(';
}

static int isCloser(const char c)
{
    return c == ']'
        || c == '}'
        || c == ')';
}

static char openerToCloser(const char c)
{
    switch (c)
    {
        case '[': return ']';
        case '{': return '}';
        case '(': return ')';
        default: return 0;
    }
}