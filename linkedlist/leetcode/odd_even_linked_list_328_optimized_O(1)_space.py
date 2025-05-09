# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        temp = head
        if not head:
            return None
        prev = temp
        odd_ll = ListNode(0)
        root = odd_ll

        while temp is not None:
            if i % 2 == 0:
                prev = temp
                temp = temp.next
            else:
                root.next = temp
                root = temp
                temp = temp.next
                prev.next = temp
            i += 1

        # IMPORTANT: terminate even list
        root.next = None
        prev.next = odd_ll.next
        return head
