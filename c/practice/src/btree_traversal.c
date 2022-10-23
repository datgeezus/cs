#include <stdint.h>
#include <string.h>
#include <malloc.h>
#include "deque/deque.h"
#include "result/result.h"
#include "optional/optional.h"


struct node
{
    int value;
    Optional left;
    Optional right;
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
        Result curr = Deque_PopLeft(deque);
        if (RESULT_IS_OK(curr))
        {
            Node *node = (Node *)curr.value;
            printf("Node: %d\n", node->value);
            if (Optional_IsPresent(node->left))
            {
                Deque_Append(deque, Optional_Get(node->left));
            }
            if (Optional_IsPresent(node->right))
            {
                Deque_Append(deque, Optional_Get(node->right));
            }
        }
        else
        {
            printf("ERR: %d", curr.type);
        }
    }



    if(Optional_IsPresent(n2.left))
    {
        Node *left = (Node *)Optional_Get(n2.left);
        printf("n2 value:%d\n", left->value);
    }

    if(!Optional_IsPresent(n4.right))
    {
        printf("n4 has no right nodes\n");
    }

    printf("n1 value:%d\n", n1.value);
}

static void node__init(Node *This, int value)
{
    This->value = value;
    This->left = Optional_Empty();
    This->right = Optional_Empty();
}

static Node node__new(int value)
{
    Node n;
    n.value = value;
    n.left = Optional_Empty();
    n.right = Optional_Empty();
    return n;
}

static void node__add_left(Node *This, Node *That)
{
    This->left = Optional_Of(That);
}

static void node__add_right(Node *This, Node *That)
{
    This->right = Optional_Of(That);
}



