from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_mapping = Counter(nums)
        n = len(nums)
        result = []
        freq_arr = [-1] * (n + 1)

        for num, freq in freq_mapping.items():
            if freq_arr[freq] == -1:
                freq_arr[freq] = [num]
            else:
                freq_arr[freq].append(num)

        count = 0
        for i in range(n, -1, -1):
            if freq_arr[i] == -1:
                continue
            result.extend(freq_arr[i])
            count += len(freq_arr[i])
            if count == k:
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
