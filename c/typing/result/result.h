#ifndef _RESULT_H_
#define _RESULT_H_

enum ResultType
{
    RESULT_OK,
    RESULT_ERR
};

typedef struct result Result;

struct result
{
    enum ResultType type;
    void* value;
};

#define RESULT_IS_OK(result) ((result.type) == RESULT_OK)

#endif