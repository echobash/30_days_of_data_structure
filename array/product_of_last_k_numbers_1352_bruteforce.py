class ProductOfNumbers:

    def __init__(self):
        self.num_list = []
        self.length = 0

    def add(self, num: int) -> None:
        self.num_list.append(num)
        self.length += 1

    def getProduct(self, k: int) -> int:
        # 3 0 2 5 4
        # 0 1 2 3 4
        # len = 5 = n
        # 0 0 40 20 4
        product = 1
        for i in range(self.length-1,self.length-1-k,-1):
            product *= self.num_list[i]
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)