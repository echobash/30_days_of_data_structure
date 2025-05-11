# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getLength(self, temp):
        size = 0
        while temp is not None:
            size += 1
            temp = temp.next
        return size

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.getLength(l1)
        n2 = self.getLength(l2)

        smaller = bigger = None
        if n1 <= n2:
            smaller = l1
            bigger = l2
        else:
            smaller = l2
            bigger = l1

        temp1 = smaller
        temp2 = bigger
        carry = 0

        """
        We are running outer loop on smaller LL and then one another loop for remaining nodes in bigger LL
        """
        while temp1 is not None:
            sum = temp1.val + temp2.val + carry
            temp2.val = sum % 10
            carry = sum // 10

            # Equal length LLs
            if temp1.next is None and temp2.next is None:
                if carry != 0:
                    temp2.next = ListNode(carry)
                return bigger

            temp1 = temp1.next
            temp2 = temp2.next

        while temp2 is not None:
            sum = temp2.val + carry
            temp2.val = sum % 10
            carry = sum // 10
            if temp2.next is None and carry != 0:
                temp2.next = ListNode(carry)
                return bigger
            temp2 = temp2.next
        return bigger
