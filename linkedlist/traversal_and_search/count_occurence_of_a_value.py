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

    def count_occurrences(self,search_value):
        total_count = 0
        temp = self.head
        while temp:
            if temp.data == search_value:
                total_count += 1
            temp = temp.next
        return total_count


ll = LinkedList()
data = [12, 9, 15, 9, 20, 9]

for value in data:
    ll.append(value)

print(ll.count_occurrences(9))
