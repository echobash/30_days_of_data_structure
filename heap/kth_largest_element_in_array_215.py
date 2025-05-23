import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappushpop(heap, num)
                    # heapq.heappop(heap)
                    # heapq.heappush(heap, num)
        return heap[0]


sol = Solution()

nums = [10, 9, 4, 2, 7, 5, 1, 6, 0, 3, 8]
k = 8
print(f"{nums = } {sol.findKthLargest(nums, k) = }")

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(f"{nums = } {sol.findKthLargest(nums, k) = }")

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(f"{nums = } {sol.findKthLargest(nums, k) = }")
