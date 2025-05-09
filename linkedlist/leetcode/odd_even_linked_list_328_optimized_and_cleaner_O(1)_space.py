# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        even = head
        odd_head = head.next
        odd = odd_head

        while odd is not None and odd.next is not None:
            even.next = odd.next
            even = even.next

            odd.next = even.next
            odd = odd.next
        even.next = odd_head
        return head

