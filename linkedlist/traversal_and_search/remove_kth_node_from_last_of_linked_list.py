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

    def delete_kth_node_from_last(self, k, n):
        if k > n:
            print(f"Not enough number of nodes in LinkedList {k = } {n = }")
            return
        if not self.head:
            print("Can't find the LinkedList. It's already empty")
            return

        slow = self.head
        fast = self.head

        if not self.head:
            print("Can't find the LinkedList. It's already empty")
            return


        for _ in range(k):
            fast = fast.next

        if fast is None:
            self.head = self.head.next
            return

        # While loop will stop as soon as
        # The fast is None
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next


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

# data = [1,2,3,4,5,6,7,8,9]
data = [1,2]
for value in data:
    ll.append(value)

ll.printLL()
k = 2

ll.delete_kth_node_from_last(k,len(data))


ll.printLL()

# data = [1,2,3,4,5,6,7,8]
# for value in data:
#     ll.append(value)
#
# ll.printLL()
# print(f"Middle of the linkedList {data=} is {ll.find_middle().data}")
