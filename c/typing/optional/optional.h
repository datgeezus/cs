#ifndef _OPTIONAL_H_
#define _OPTIONAL_H_

enum OptionalType
{
    OPTIONAL_PRESENT,
    OPTIONAL_EMPTY
};

struct optional
{
    enum OptionalType type;
    void *value;
};

struct optionalInt
{
    enum OptionalType type;
    int value;
};

#define EMP


typedef struct optional Optional;
typedef struct optionalInt OptionalInt;

int Optional_IsPresent(Optional optional);
OptionalInt OptionalInt_Of(int value);
Optional Optional_Of(void *value);
Optional Optional_Empty();
Optional OptionalInt_Empty();
void *Optional_Get(Optional optional);
void *Optional_GetOrElse(Optional optional, void *value);
int OptionalInt_Get(OptionalInt optional);
Optional Optional_Map(Optional optional, void*(*fn)(void *), void *value);

#endif