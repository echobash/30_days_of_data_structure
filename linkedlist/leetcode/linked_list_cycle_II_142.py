# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        if not head:
            return None

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                # When slow and fast meet, reset slow to head and move slow and fast one step at a time
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None