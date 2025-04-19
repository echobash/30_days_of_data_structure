class Node:
    def __init__(self,data ):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count_nodes = 0

    def insert_at_head(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_position(self,position, data):
        # First Reach at that position
        # Create a Node
        # Keep track of prev node and current(temp) node
        # Break link between previous node and the current node
        # Point the new node as next to previous node
        # Point the new node's next as the current node
        if position < 1 or position > self.getLength() + 1:
            print("Can't insert. LinkedList too long or invalid position")
            return
        pos = 1
        temp = self.head
        prev = None
        if position == 1:
            self.insert_at_head(data)
            return
        while temp is not None:
            if pos == position:
                node = Node(data)
                node.next = temp
                prev.next = node
                return
            else:
                pos += 1
            prev = temp
            temp = temp.next

        # Check if the node is to be inserted at the tail
        node = Node(data)
        prev.next = node




    def printLL(self):
        temp = self.head
        print(f"LinkedList = ",end="")
        while temp is not None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print(None)

    def getLength(self):
        self.count_nodes = 0
        temp = self.head
        while temp is not None:
            self.count_nodes += 1
            temp = temp.next
        return self.count_nodes


ll = LinkedList()
ll.insert_at_head(10)
ll.insert_at_head(20)
ll.insert_at_head(30)
ll.insert_at_head(40)
ll.insert_at_head(50)
ll.insert_at_head(60)
ll.printLL()
ll.insert_at_position(3,44)
ll.printLL()
ll.insert_at_position(3,11)
ll.printLL()
print(f"Length = {ll.getLength()}")
ll.insert_at_position(8,100)
ll.printLL()
print(f"Length = {ll.getLength()}")
ll.insert_at_position(10,1000)
ll.printLL()
print(f"Length = {ll.getLength()}")
