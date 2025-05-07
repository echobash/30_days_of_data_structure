from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        temp = head

        even_ll = ListNode(0)
        temp1 = even_ll

        odd_ll = ListNode(0)
        temp2 = odd_ll

        while temp is not None:
            if i % 2 == 0:
                temp1.next = ListNode(temp.val)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(temp.val)
                temp2 = temp2.next
            temp = temp.next
            i += 1

        even_ll = even_ll.next
        odd_ll = odd_ll.next
        temp1.next = odd_ll
        return even_ll
