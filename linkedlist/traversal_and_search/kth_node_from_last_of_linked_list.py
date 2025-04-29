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

    def find_kth_node_from_last(self, k, n):
        if k > n:
            print(f"Not enough number of nodes in LinkedList {k = } {n = }")
            return
        if not self.head:
            print("Can't find the LinkedList. It's already empty")
            return

        slow = self.head
        fast = self.head

        for _ in range(k):
            fast = fast.next

        if not self.head:
            print("Can't find the LinkedList. It's already empty")
            return

        if not self.head.next:
            print("There is only one node in the LinkedList. So the middle is itself only")
            return self.head
        # While loop will stop as soon as
        # The fast is None
        while fast is not None:
            slow = slow.next
            fast = fast.next
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
k = 3

if not data or len(data) < k:
    ll.find_kth_node_from_last(k,len(data))
else:
    print(f"{k}th node from last of the linkedList {data=} is {ll.find_kth_node_from_last(k, len(data)).data}")

# data = [1,2,3,4,5,6,7,8]
# for value in data:
#     ll.append(value)
#
# ll.printLL()
# print(f"Middle of the linkedList {data=} is {ll.find_middle().data}")
