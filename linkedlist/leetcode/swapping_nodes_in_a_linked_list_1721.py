# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        temp2 = head
        start = head
        first_value = 0
        second_value = 0
        # For finding kth node from last, we'll advance temp to k node from starting
        # Then we'll move temp and temp2 simulatenously
        # Once temp reaches to None (tail), temp2 will be at kth node from last

        count = 0
        while count != k:
            temp = temp.next
            count += 1

        while temp is not None:
            temp = temp.next
            temp2 = temp2.next

        # Now temp2 is at kth node from last
        second_value = temp2.val
        # Get kth node from start value. Move start_node k steps

        count = 1
        while count != k:
            start = start.next
            count += 1

        first_value = start.val

        start.val = second_value
        temp2.val = first_value

        return head