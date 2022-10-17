#include <stdint.h>
#include <string.h>
#include <malloc.h>
#include "deque/deque.h"

enum OptionalType
{
    PRESENT,
    EMPTY
};

struct optional
{
    void *data;
    enum OptionalType type;
};


struct node
{
    int value;
    struct optional left;
    struct optional right
};

typedef struct node Node;

static Node node__new(int value);
static void node__init(Node *This, int value);
static void node__add_left(Node *This, Node *That);
static void node__add_right(Node *This, Node *That);


int main() {

    Node n1 = node__new(1);
    Node n2 = node__new(2);
    Node n3 = node__new(3);
    Node n4 = node__new(4);

    node__add_left(&n1, &n2);
    node__add_right(&n1, &n3);
    node__add_left(&n2, &n4);

    Deque *deque = Deque_New();
    Deque_Append(deque, &n1);
    printf("Deque is empty: %d\n", Deque_IsEmpty(deque));
    while(!Deque_IsEmpty(deque))
    {
        DequeResult curr = Deque_PopLeft(deque);
        if (OK == curr.type)
        {
            Node *node = (Node *)curr.value;
            printf("Node: %d\n", node->value);
            if (PRESENT == node->left.type)
            {
                Deque_Append(deque, node->left.data);
            }
            if (PRESENT == node->right.type)
            {
                Deque_Append(deque, node->right.data);
            }
        }
        else
        {
            printf("ERR: %d", curr.type);
        }
    }



    if(n2.left.type == PRESENT)
    {
        Node *left = (Node *)n2.left.data;
        printf("n2 value:%d\n", left->value);
    }

    if(n4.right.type == EMPTY)
    {
        printf("n4 has no right nodes\n");
    }

    printf("n1 value:%d\n", n1.value);
}

static void node__init(Node *This, int value)
{
    This->value = value;
    This->left.type = EMPTY;
    This->right.type = EMPTY;
}

static Node node__new(int value)
{
    Node n;
    n.value = value;
    n.left.type = EMPTY;
    n.right.type = EMPTY;
    return n;
}

static void node__add_left(Node *This, Node *That)
{
    This->left.type = PRESENT;
    This->left.data = That;
}

static void node__add_right(Node *This, Node *That)
{
    This->right.type = PRESENT;
    This->right.data = That;
}



