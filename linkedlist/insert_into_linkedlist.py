class Node:
    def __init__(self,data ):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print(None)


ll = LinkedList()
ll.insert_at_head(1)
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.printLL()
