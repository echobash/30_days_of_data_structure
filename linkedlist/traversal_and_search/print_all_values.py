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

    def to_list(self):
        result = []
        temp = self.head
        while temp:  # same as while temp is not None but handles false, "", etc
            result.append(temp.data)
            temp = temp.next
        return result


ll = LinkedList()
ll.append(12)
ll.append(9)
ll.append(15)
ll.append(17)
ll.append(20)
ll.append(44)

print(ll.to_list())
