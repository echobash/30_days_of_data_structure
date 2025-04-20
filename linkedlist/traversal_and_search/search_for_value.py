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

    def search(self,search_value):
        index = 0
        temp = self.head
        while temp:
            if temp.data == search_value:
                return index
            else:
                index += 1
                temp = temp.next
        return -1


ll = LinkedList()
data = [12,9,15,17,20,44]

for value in data:
    ll.append(value)

print(ll.search(17))
