#include <stdint.h>
#include <malloc.h>
#include <stdlib.h>
#include "deque.h"



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

DequeResult Deque_PopLeft(Deque *deque)
{
    DequeResult result;
    if(Deque_IsEmpty(deque))
    {
        result.type = ERR;
    }
    else
    {
        result.value = deque->tail->value;
        result.type = OK;
        deque__delete_tail(deque);
    }

    return result;
}

DequeResult Deque_Pop(Deque *deque)
{
    DequeResult result;
    if(Deque_IsEmpty(deque))
    {
        result.type = ERR;
    }
    else
    {
        result.value = deque->head->value;
        result.type = OK;
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