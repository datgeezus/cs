"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

 

Constraints:

    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100

"""

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next: 'ListNode' | None = None

def swap_pairs(head: None | ListNode) -> None | ListNode:
    if not head or not head.next:
        return head

    node_one = head
    node_two = head.next

    node_one.next = swap_pairs(node_two.next)
    node_two.next = node_one

    return node_two


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(head)
    print(swap_pairs(head))
