"""
# Problem
Given the head of a singly linked list, reverse the list, and return the reversed list

# Solution
Use 2 pinters to update list order
"""


from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = None


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    prev = None
    curr = head

    while curr:
        tnext = curr.next
        curr.next = prev
        prev = curr
        curr = tnext

    return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    assert reverse(head) == res
