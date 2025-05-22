# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Use slow and fast pointer to find the middle of the list
        # Reverse the other half of the linked list from "middle"
        # Now take sum correspondingly

        # If there is only one node, return its value
        if not head.next:
            return head.val

        slow = head
        fast = head

        while fast is not None:  # n is even as per question so we won't need fast.next is not None
            slow = slow.next
            fast = fast.next.next

        # middle = slow
        prev = None
        while slow is not None:
            future = slow.next
            slow.next = prev
            prev = slow
            slow = future
        secondHalfReversedHead = prev

        temp1 = head
        temp2 = secondHalfReversedHead
        max_sum = 0
        curr_sum = 0
        while temp2 is not None:
            curr_sum = temp2.val + temp1.val
            temp2 = temp2.next
            temp1 = temp1.next
            max_sum = max(curr_sum, max_sum)
        return max_sum