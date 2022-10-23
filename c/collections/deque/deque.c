#include <stdint.h>
#include <malloc.h>
#include <stdlib.h>
#include "deque.h"
#include "optional/optional.h"



struct node
{
    void *value;
    struct node *prev;
    struct node *next;
};

struct deque
{
    struct node *head;
    struct node *tail;
    int isEmpty;
    size_t size;
};

typedef struct node Node;
static Node* node__new(void *value);
static void deque__delete_tail(Deque *deque);
static void deque__delete_head(Deque *deque);
static void deque__decrement_size(Deque *deque);

Deque *Deque_New()
{
    Deque *deque = calloc(1, sizeof(Deque));
    deque->size = 0;
    deque->isEmpty = 1;
    return deque;
}

void Deque_Append(Deque* deque, void *value)
{
    Node *new = node__new(value);
    Node *head = deque->head;

    if(Deque_IsEmpty(deque))
    {
        deque->head = new;
        deque->tail = new;
    }
    else
    {
        head->next = new;
        deque->head = new;
    }
    deque->size += 1;
}

Result Deque_PopLeft(Deque *deque)
{
    Result result;
    if(Deque_IsEmpty(deque))
    {
        result.type = RESULT_ERR;
    }
    else
    {
        result.value = deque->tail->value;
        result.type = RESULT_OK;
        deque__delete_tail(deque);
    }

    return result;
}

Result Deque_Pop(Deque *deque)
{
    Result result;
    if(Deque_IsEmpty(deque))
    {
        result.type = RESULT_ERR;
    }
    else
    {
        result.value = deque->head->value;
        result.type = RESULT_OK;
        deque__delete_head(deque);
    }

    return result;
}

int Deque_IsEmpty(Deque *deque)
{
    return deque->size <= 0;
}


static Node* node__new(void *value)
{
    Node *node = calloc(1, sizeof(Node));
    node->value = value;
    return node;
}


static void deque__delete_tail(Deque *deque)
{
    Node* tail = deque->tail;
    if(NULL != tail)
    {
        deque->tail = tail->next;
        deque__decrement_size(deque);
        free(tail);
    }
}

static void deque__delete_head(Deque *deque)
{
    Node* head = deque->head;
    if (NULL != head)
    {
        deque->head = head->prev;
        deque__decrement_size(deque);
        free(head);
    }
}

static void deque__decrement_size(Deque *deque)
{
    int currSize = deque->size;
    if(currSize > 0)
    {
        deque->size -= 1;
    }
}


/**
 * Deque Optional
*/


struct nodeopt
{
    void *value;
    Optional prev;
    Optional next;
};

struct dequeopt
{
    Optional head;
    Optional tail;
    int isEmpty;
    size_t size;
};

typedef struct nodeopt NodeOpt;
typedef struct dequeopt DequeOpt;
static NodeOpt* nodeopt__new(void *value);
static void dequeopt__delete_tail(DequeOpt *deque);
static void dequeopt__delete_head(DequeOpt *deque);
static void dequeopt__decrement_size(DequeOpt *deque);

DequeOpt *DequeOpt_New()
{
    DequeOpt *deque = calloc(1, sizeof(DequeOpt));
    deque->size = 0;
    deque->isEmpty = 1;
    return deque;
}

void DequeOpt_Append(DequeOpt* deque, void *value)
{
    deque->head = Optional_Map(deque->head, node__new, value);
    deque->size += 1;
}

Result DequeOpt_PopLeft(DequeOpt *deque)
{
    Result result;
    if(Deque_IsEmpty(deque))
    {
        result.type = RESULT_ERR;
    }
    else
    {
        result.value = Optional_Get(deque->tail);
        result.type = RESULT_OK;
        deque__delete_tail(deque);
    }

    return result;
}
