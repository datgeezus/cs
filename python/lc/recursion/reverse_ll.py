"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

 

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

"""

from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next: 'ListNode | None' = None

def revese_list(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head

    tmp = revese_list(head.next)
    head.next.next = head
    head.next = None
    return tmp


if __name__ == "__main__":
    h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(h)
    print(revese_list(h))
