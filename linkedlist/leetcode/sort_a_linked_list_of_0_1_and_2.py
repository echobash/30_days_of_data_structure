class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None


class Solution:
    def segregate(self, head):
        count0 = 0
        count1 = 0
        count2 = 0

        temp = head
        while temp is not None:
            if temp.data == 0:
                count0 += 1
            elif temp.data == 1:
                count1 += 1
            else:
                count2 += 1
            temp = temp.next

        temp = head
        for _ in range(count0):
            temp.data = 0
            temp = temp.next

        for _ in range(count1):
            temp.data = 1
            temp = temp.next

        for _ in range(count2):
            temp.data = 2
            temp = temp.next

        return head
