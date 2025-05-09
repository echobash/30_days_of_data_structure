from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visted_set = set()
        temp1 = headA
        temp2 = headB

        while temp1 is not None:
            visted_set.add(temp1)
            temp1 = temp1.next

        while temp2 is not None:
            if temp2 in visted_set:
                return temp2
            visted_set.add(temp2)
            temp2 = temp2.next
        return None
