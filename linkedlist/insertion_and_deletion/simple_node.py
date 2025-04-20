class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


n1 = Node(4)
n2 = Node(6)
n3 = Node(8)
n4 = Node(10)

n1.next = n2
n2.next = n3
n3.next = n4

class LinkedList:
    def __init__(self,head):
        self.head = head

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print(None)


ll = LinkedList(n1)
ll.printLL()