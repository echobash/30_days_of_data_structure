class ProductOfNumbers:

    def __init__(self):
        self.num_list = []
        self.length = 0

    def add(self, num: int) -> None:
        if self.length == 0:
            self.num_list.append(num)
        else:
            for i in range(self.length):
                self.num_list[i] *= num
            self.num_list.append(num)

        self.length += 1

    def getProduct(self, k: int) -> int:
        # 3 6 2 5 4
        # 0 1 2 3 4
        # len = 5 = n
        # 720,240,40,20,4

        return self.num_list[self.length - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)