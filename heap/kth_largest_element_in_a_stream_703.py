import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            else:
                if num > self.heap[0]:
                    heapq.heapreplace(self.heap, num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


sol = KthLargest(3, [4, 5, 8, 2])
print(sol.add(3))
print(sol.add(5))
print(sol.add(10))
print(sol.add(9))
print(sol.add(4))
print()

sol = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(sol.add(2))
print(sol.add(10))
print(sol.add(9))
print(sol.add(9))
