# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_list = []

        if not head:
            return False

        # Store nodes in a list as it is
        temp = head
        while temp is not None:
            node_list.append(temp.val)
            temp = temp.next

        # Reverse the LL
        temp = head
        prev = None
        while temp is not None:
            future = temp.next
            temp.next = prev
            prev = temp
            temp = future
        head = prev

        # Store the reversed nodes in new list
        reversed_node_list = []
        temp = head
        while temp is not None:
            reversed_node_list.append(temp.val)
            temp = temp.next

        return reversed_node_list == node_list
