import heapq
from typing import List


class Solution:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, -1*num)
            else:
                if -1*num > heap[0]:
                    heapq.heapreplace(heap, -1*num)
        return -1*heap[0]


sol = Solution()

nums = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{nums = } {sol.findKthSmallest(nums, k) = }")

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"{nums = } {sol.findKthSmallest(nums, k) = }")

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(f"{nums = } {sol.findKthSmallest(nums, k) = }")
