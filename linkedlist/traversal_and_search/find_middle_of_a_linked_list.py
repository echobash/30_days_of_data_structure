class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def printLL(self):
        temp = self.head
        print(f"LinkedList = ",end="")
        while temp is not None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print(None)
        print("-------------------------------------------------")

    def append(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            self.temp.next = node
        self.temp = node

    def find_middle(self):
        slow = self.head
        fast = self.head

        if not self.head:
            print("Can't find the LinkedList. It's already empty")
            return

        if not self.head.next:
            print("There is only one node in the LinkedList. So the middle is itself only")
            return self.head
        # print(f"{fast.data} {fast.next.data}  {slow.data} {slow.next.data}")
        print(f"before {slow.data = } {fast.data =}")
        # While loop will stop as soon as
        # a. Either the fast is None
        # b. fast.next is None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


ll = LinkedList()

# data = [6]
# for value in data:
#     ll.append(value)
#
# print(f"Middle of the linkedList {data=} is {ll.find_middle().data if data else None}")
#
# data = []
# for value in data:
#     ll.append(value)
#
# print(f"Middle of the linkedList {data=} is {ll.find_middle().data if data else None}")

data = [1,2,3,4,5,6,7,8,9]
for value in data:
    ll.append(value)

ll.printLL()
print(f"Middle of the linkedList {data=} is {ll.find_middle().data}")

# data = [1,2,3,4,5,6,7,8]
# for value in data:
#     ll.append(value)
#
# ll.printLL()
# print(f"Middle of the linkedList {data=} is {ll.find_middle().data}")
