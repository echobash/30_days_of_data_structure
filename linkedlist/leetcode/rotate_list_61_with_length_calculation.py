from typing import Optional


# Definition for singly-linked list.
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

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = self.getLength(head)
        i = 0
        newHead = None
        prevNewHead = None
        last = None
        temp = head

        if not head:
            return None

        k = k % n

        if k == 0 or n == 1:
            return head

        while temp is not None:
            last = temp
            i += 1
            if i == (n - k):
                prevNewHead = temp
            if i == (n - k + 1):
                newHead = temp
                print(newHead.val)
            temp = temp.next

        last.next = head
        head = newHead
        prevNewHead.next = None
        return head

head = [1,2,3,4,5]
k = 2

head = [0,1,2]
k = 4

head = []
k = 4

head = [1]
k = 4

head = [1,2,3,4,5]
k = 21

head = [1,2,3,4,5]
k = 20
