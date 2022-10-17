#ifndef _RESULT_H_
#define _RESULT_H_

enum ResultType
{
    OK,
    ERR
};

typedef struct result Result;

struct result
{
    ResultType type;
    void* data;
};

#endif