# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # slow points to the mid of the LL
        # For odd length LL, we can skip the exact middle one as it does not matter
        if fast is not None:
            slow = slow.next

        prev = None
        while slow is not None:
            future = slow.next
            slow.next = prev
            prev = slow
            slow = future

        slow = prev
        temp3 = head
        while temp3 is not None and slow is not None:
            if temp3.val != slow.val:
                return False
            temp3 = temp3.next
            slow = slow.next
        return True
