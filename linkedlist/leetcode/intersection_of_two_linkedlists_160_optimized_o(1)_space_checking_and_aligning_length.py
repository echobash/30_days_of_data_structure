from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB

        length1 = 0
        length2 = 0
        while temp1 is not None:
            length1 += 1
            temp1 = temp1.next

        while temp2 is not None:
            length2 += 1
            temp2 = temp2.next

        if length1 >= length2:
            larger_linkedlist = headA
            smaller_linkedlist = headB
        else:
            larger_linkedlist = headB
            smaller_linkedlist = headA

        length_diff = abs(length1 - length2)

        for _ in range(length_diff):
            larger_linkedlist = larger_linkedlist.next

        # Now both the linkedlists are of same length
        while larger_linkedlist is not None:
            print(f"{larger_linkedlist.val = } {smaller_linkedlist.val = }")
            if larger_linkedlist == smaller_linkedlist:
                return smaller_linkedlist
            larger_linkedlist = larger_linkedlist.next
            smaller_linkedlist = smaller_linkedlist.next
        return None

