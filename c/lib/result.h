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
    enum ResultType type;
    void* data;
};

#define RESULT_IS_OK(result) ((result.type) == OK)

#endif