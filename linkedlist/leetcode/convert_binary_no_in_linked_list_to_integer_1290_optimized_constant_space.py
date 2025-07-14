from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        result = 0

        while temp is not None:
            result = result << 1 # Left Shift 1 space. Since result is initially 0, so it doesn't affect
            result = result | temp.val # Taking OR with current no appends the no in right
            temp = temp.next # Switch to next node
        return result # Result already returned in decimal

