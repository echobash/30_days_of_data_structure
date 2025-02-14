class ProductOfNumbers:

    def __init__(self):
        self.num_list = []
        self.length = 0
        self.prod = 1
        self.found_zero_at = -1

    def add(self, num: int) -> None:
        self.length += 1
        if num != 0:
            self.prod *= num
            self.num_list.append(self.prod)
        else:
            self.num_list.append(1)
            self.prod = 1
            self.found_zero_at = self.length - 1

    def getProduct(self, k: int) -> int:
        if self.found_zero_at != -1 and k >= self.length - self.found_zero_at:
            return 0
        if self.length == k:
            return self.num_list[self.length - 1]
        return self.num_list[self.length-1] // self.num_list[self.length - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)