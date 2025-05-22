class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def segregate(self, head):
        temp = head
        zero_head = Node(-1)
        zero_dummy = zero_head
        one_head = Node(-1)
        one_dummy = one_head
        two_head = Node(-1)
        two_dummy = two_head

        while temp is not None:
            if temp.data == 0:
                zero_dummy.next = temp
                zero_dummy = zero_dummy.next
            elif temp.data == 1:
                one_dummy.next = temp
                one_dummy = one_dummy.next
            else:
                two_dummy.next = temp
                two_dummy = two_dummy.next
            temp = temp.next

        if zero_head.next:  # zero is present
            head = zero_head.next
            if one_head.next:
                zero_dummy.next = one_head.next
                one_dummy.next = two_head.next
            else:
                zero_dummy.next = two_head.next
        elif one_head.next:
            head = one_head.next
            one_dummy.next = two_head.next
        elif two_head.next:
            head = two_head.next
        two_dummy.next = None

        return head
