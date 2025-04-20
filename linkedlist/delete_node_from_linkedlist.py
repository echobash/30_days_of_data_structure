class Node:
    def __init__(self,data ):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count_nodes = 0


    def printLL(self):
        temp = self.head
        print(f"LinkedList = ",end="")
        while temp is not None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print(None)
        print("-------------------------------------------------")

    def getLength(self):
        self.count_nodes = 0
        temp = self.head
        while temp is not None:
            self.count_nodes += 1
            temp = temp.next
        return self.count_nodes

    def deleteHead(self):
        if not self.head:
            print("Can't delete. The LinkedList is already empty")
            return
        else:
            print(f"Deleted head node with data = {self.head.data}")
            self.head = self.head.next

    def deleteTail(self):
        # 12->9->15->17->20->44->None
        # Empty LL Edge case
        if not self.head:
            print("Can't delete. The LinkedList is already empty")
            return

        # One one node LL Edge case
        if self.head.next is None:
            self.head = None
            return

        # Move pointer by 2. and we'll reach on 2nd last once temp reaches to None
        temp = self.head

        while temp.next.next:
            temp = temp.next
        temp.next = None

    def append(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.temp = self.head
        else:
            self.temp.next = node
            self.temp = self.temp.next


ll = LinkedList()
ll.append(12)
ll.append(9)
ll.append(15)
ll.append(17)
ll.append(20)
ll.append(44)
ll.printLL()

# ll.deleteHead()
# ll.printLL()
#
# ll.deleteHead()
# ll.printLL()
#
# ll.deleteHead()
# ll.printLL()
#
# ll.deleteHead()
# ll.printLL()
#
# ll.deleteHead()
# ll.printLL()
#
# ll.deleteHead()
# ll.printLL()

ll.deleteTail()
ll.printLL()

ll.deleteTail()
ll.printLL()

ll.deleteTail()
ll.printLL()

ll.deleteTail()
ll.printLL()

ll.deleteTail()
ll.printLL()

ll.deleteTail()
ll.printLL()

ll.deleteTail()
ll.printLL()
