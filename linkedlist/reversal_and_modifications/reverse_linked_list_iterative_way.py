class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def append(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            self.temp.next = node
        self.temp = node

    def printLL(self):
        temp = self.head
        print(f"LinkedList = ",end="")
        while temp is not None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print(None)
        print("-------------------------------------------------")

    def reverse(self):
        temp = self.head
        prev = None
        while temp is not None:
            future = temp.next
            temp.next = prev
            prev = temp
            temp = future
        self.head = prev
        print("Reversed-", end="")
        self.printLL()


ll = LinkedList()
data = [12, 9, 15, 17, 20, 44]

for value in data:
    ll.append(value)

ll.printLL()
ll.reverse()
