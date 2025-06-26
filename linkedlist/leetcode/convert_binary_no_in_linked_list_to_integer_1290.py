from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        bit_list = []
        temp = head

        while temp is not None:
            bit_list.append(str(temp.val))
            temp = temp.next
        binary_string = "".join(bit_list)

        return int(binary_string, 2)

