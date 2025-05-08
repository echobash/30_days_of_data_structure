class MinStack:

    def __init__(self):
        self.data = []
        self.min_data = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.min_data) == 0:
            self.min_data.append(val)
        else:
            self.min_data.append(min(self.min_data[-1],val))

    def pop(self) -> None:
        self.data.pop()
        self.min_data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_data[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
