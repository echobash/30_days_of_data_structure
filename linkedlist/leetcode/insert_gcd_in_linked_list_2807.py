from math import gcd
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getGcd(self, x, y):
        return gcd(x, y)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        temp = head
        future = head.next

        while temp.next is not None:
            temp.next = ListNode(self.getGcd(temp.val, temp.next.val))
            temp.next.next = future
            temp = temp.next.next
            future = future.next
        return head

