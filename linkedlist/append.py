class Node:
    def __init__(self,data ):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print(None)

    def append(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.temp = self.head
        else:
            self.temp.next = node
            self.temp = self.temp.next

    def insert_at_head(self,data):
        node = Node(data)
        node.next = self.head
        if not self.temp:
            self.temp = self.head
        self.head = node

ll = LinkedList()
ll.insert_at_head(786)
ll.insert_at_head(78)
ll.append(999)
ll.insert_at_head(22)
ll.printLL()
