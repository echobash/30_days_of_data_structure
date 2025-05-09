from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB

        if not headA or not headB:
            return None

        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next

            if temp1 is None and temp2 is None:
                return None

            if temp1 is None:
                temp1 = headB

            if temp2 is None:
                temp2 = headA
        return temp1
