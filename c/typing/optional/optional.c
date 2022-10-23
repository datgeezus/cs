#include "optional.h"


OptionalInt OptionalInt_Of(int value)
{
    OptionalInt optional;
    optional.type = OPTIONAL_PRESENT;
    optional.value = value;
    return optional;
}

Optional Optional_Of(void *value)
{
    Optional optional;
    optional.type = OPTIONAL_PRESENT;
    optional.value = value;
    return optional;
}

Optional Optional_Empty()
{
    Optional optional;
    optional.type = OPTIONAL_EMPTY;
    return optional;
}

Optional Optional_Map(Optional optional, void*(*fn)(void *), void *value)
{
    Optional ret = optional;
    if (Optional_IsPresent(optional))
    {
        ret = Optional_Of(fn(value));
    }

    return ret;
}

void *Optional_GetOrElse(Optional optional, void *value)
{
    if (Optional_IsPresent(optional))
    {
        return optional.value;
    }

    return value;
}

int Optional_IsPresent(Optional optional)
{
    return OPTIONAL_PRESENT == optional.type;
}