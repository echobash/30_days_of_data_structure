from typing import List
import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Heap does not guarantee in case of duplicates. So put in set and then operate on it.
        nums = list(set(nums))
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums)

        heap = []
        for num in nums:
            if len(heap) < 3:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)
        return heap[0]


solution = Solution()

nums = [3,2,1]
print(f"{nums = } {solution.thirdMax(nums) = }")

nums = [1,2]
print(f"{nums = } {solution.thirdMax(nums) = }")

nums = [2,2,3,1]
print(f"{nums = } {solution.thirdMax(nums) = }")
