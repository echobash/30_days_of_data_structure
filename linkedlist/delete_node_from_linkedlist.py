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

    def delete_at_position(self,position):
        # 12->9->15->17->20->44->None
        if not self.head:
            print("Can't delete. The LinkedList is already empty")
            return

        if position < 1:
            print("Can't delete. Invalid Position given")
            return

        temp = self.head
        prev = None
        pos = 1

        if position == 1:
            self.deleteHead()
            return

        while temp is not None:
            if pos == position:
                print(f"Deleted node at position {position} with data = {temp.data}")
                prev.next = temp.next
                return
            else:
                prev = temp
                temp = temp.next
                pos += 1

        print("Can't delete. Position > length of linkedList")
        return

    def delete_first_occurrence_by_value(self, value):
        if not self.head:
            print("Can't delete. The LinkedList is already empty")
            return

        if value == self.head.data:
            self.deleteHead()
            return

        temp = self.head
        prev = None

        while temp:
            if temp.data == value:
                prev.next = temp.next
                return
            else:
                prev = temp
                temp = temp.next

        print(f"This value {value} doesn't exist in the LinkedList")
        return

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
ll.append(15)
ll.append(15)
ll.append(15)
ll.append(15)
ll.append(17)
ll.append(20)
ll.append(44)
ll.printLL()

# Delete Heads
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

# Delete Tails
# ll.deleteTail()
# ll.printLL()
#
# ll.deleteTail()
# ll.printLL()
#
# ll.deleteTail()
# ll.printLL()
#
# ll.deleteTail()
# ll.printLL()
#
# ll.deleteTail()
# ll.printLL()
#
# ll.deleteTail()
# ll.printLL()
#
# ll.deleteTail()
# ll.printLL()

# ll.delete_at_position(3)
# ll.printLL()
#
# ll.delete_at_position(3)
# ll.printLL()
#
# ll.delete_at_position(3)
# ll.printLL()
#
# ll.delete_at_position(3)
# ll.printLL()
#
# ll.delete_at_position(2)
# ll.printLL()
#
# ll.delete_at_position(1)
# ll.printLL()
#
# ll.delete_at_position(1)
# ll.printLL()

ll.delete_first_occurence_by_value(17)
ll.printLL()

ll.delete_first_occurence_by_value(23)
ll.printLL()

ll.delete_first_occurence_by_value(20)
ll.printLL()

ll.delete_first_occurence_by_value(12)
ll.printLL()

ll.delete_first_occurence_by_value(15)
ll.printLL()

ll.delete_first_occurence_by_value(9)
ll.printLL()

ll.delete_first_occurence_by_value(44)
ll.printLL()

ll.delete_first_occurence_by_value(12)
ll.printLL()






