'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow = head
        fast = head

        count = 0
        if not head:
            return count

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                # When slow and fast meet, keep slow as it is and move fast one step at a time
                # and keep incrementing the counter

                # Moved fast one step ahead and did count = 1
                # So that while slow!=fast could be triggered
                fast = fast.next
                count = 1
                while slow != fast:
                    fast = fast.next
                    count += 1
                return count
        return 0