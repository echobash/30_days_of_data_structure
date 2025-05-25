from typing import List
from collections import Counter, defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_mapping = Counter(nums)
        rev_freq_mapping = defaultdict(list)

        for num, freq in freq_mapping.items():
            rev_freq_mapping[freq].append(num)

        heap = []
        for num in freq_mapping.values():
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heapreplace(heap, num)

        result = []
        unique_heap_freq = list(set(heap))
        count = 0
        for freq in unique_heap_freq:
            for val in rev_freq_mapping[freq]:
                result.append(val)
        return result


sol = Solution()

nums = [1,1,1,2,2,3]
k = 2
print(f"{nums = } {sol.topKFrequent(nums, k) = }")

nums = [1,1,1,2,2,3]
k = 2
print(f"{nums = } {sol.topKFrequent(nums, k) = }")

nums = [1]
k = 1
print(f"{nums = } {sol.topKFrequent(nums, k) = }")

nums = [1,1,1,1,1,2,2,2,3,3,3,3,3,3,3,3]
k = 2
print(f"{nums = } {sol.topKFrequent(nums, k) = }")
