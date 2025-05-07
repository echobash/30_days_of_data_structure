# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_data = []
        temp = head
        if not head:
            return None
        while temp is not None:
            list_data.append(temp.val)
            temp = temp.next

        list_data = sorted(list_data)
        # list_data has sorted data. Now convert it into linkedlist and return its head

        n = len(list_data)

        dummy = ListNode(list_data[0])
        temp = dummy

        for i in range(n):
            temp.next = ListNode(list_data[i])
            temp = temp.next

        # dummy.next is our new head
        return dummy.next


