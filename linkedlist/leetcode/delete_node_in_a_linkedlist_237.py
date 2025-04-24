# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        We only have the "to be deleted Node address", so we can't traverse all the way from the head.
        So we will just have to overwrite the "to be deleted Node" by its next node value.
        Also we will need to point the next of this "To be deleted Node" to node.next.next  since node.next will have the same value since we just copied it into the "to be deleted node"
        """

        node.val = node.next.val
        node.next = node.next.next