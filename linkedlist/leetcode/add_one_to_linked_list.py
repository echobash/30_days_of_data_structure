class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def addOne(self,head):
        temp = head
        prev = None

        # Reverse the linkedlist
        while temp is not None:
            future = temp.next
            temp.next = prev
            prev = temp
            temp = future
        head = prev

        #Add 1 to reversed linkedlist
        temp = head
        carry = 1
        while temp is not None:
            sum = temp.data + carry
            temp.data = sum % 10
            carry = sum // 10
            if not temp.next and carry > 0:
                temp.next = Node(carry)
                break
            temp = temp.next

        temp = head
        prev = None

        # Reverse back the linkedlist to get original one
        while temp is not None:
            future = temp.next
            temp.next = prev
            prev = temp
            temp = future
        head = prev
        return head
