"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack
"""

from collections import deque


class MinStack:
    def __init__(self):
        self.mins = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = min(val, self.mins[-1] if self.mins else val)
        self.mins.append(new_min)

    def pop(self) -> None:
        self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.mins[-1]

def test1():
    print("Test 1")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.get_min() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.get_min() == -2

def test2():
    print("Test 2")
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(0)
    assert min_stack.get_min() == 0
    min_stack.pop()
    assert min_stack.top() == 2
    assert min_stack.get_min() == 1


if __name__ == "__main__":
    test1()
    test2()
