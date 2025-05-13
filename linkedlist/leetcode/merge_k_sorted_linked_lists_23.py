# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        result = []
        for list in lists:
            temp = list
            while temp is not None:
                result.append(temp.val)
                temp = temp.next
        result = sorted(result)
        if len(result) == 0:
            return None

        dummy = ListNode(0)
        temp = dummy
        for data in result:
            temp.next = ListNode(data)
            temp = temp.next
        return dummy.next
