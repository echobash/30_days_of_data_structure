# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        temp = head

        while temp is not None and  temp.val in nums:
            temp = temp.next

        new_head = temp
        if new_head is None:
            return None

        temp2 = new_head
        temp = temp.next

        while temp is not None:
            if temp.val not in nums:
                temp2.next = temp
                temp2 = temp2.next
            temp = temp.next
        
        if temp2 is not None:
            temp2.next = None
        return new_head