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


ll = LinkedList()
ll.append(23)
ll.append(14)
ll.append(53)
ll.append(64)
ll.printLL()

