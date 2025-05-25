from typing import List
from collections import Counter, defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_mapping = Counter(nums)

        result = []
        heap = []
        for num, freq in freq_mapping.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))

        for freq, num in heap:
            result.append(num)
        return result


sol = Solution()

nums = [1,1,1,2,2,3]
k = 2
print(f"{nums = } {sol.topKFrequent(nums, k) = }")

nums = [4,4,4,5,5,3,5,2]
k = 4
print(f"{nums = } {sol.topKFrequent(nums, k) = }")

nums = [4,1,-1,2,-1,2,3]
k = 2
print(f"{nums = } {sol.topKFrequent(nums, k) = }")

nums = [1]
k = 1
print(f"{nums = } {sol.topKFrequent(nums, k) = }")

nums = [1,1,1,1,1,2,2,2,3,3,3,3,3,3,3,3]
k = 2
print(f"{nums = } {sol.topKFrequent(nums, k) = }")
