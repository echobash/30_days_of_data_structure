from typing import List
from collections import defaultdict


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Loop on queries and update total count of updation of each index
        # We know one updation will decrement the value by 1
        # We'll decrease the final count from their respective indices

        index_updation_freq_mapping = defaultdict(int)
        for query in queries:
            l, r = query[0], query[1]
            for j in range(l, r + 1):
                index_updation_freq_mapping[j] += 1

        print(index_updation_freq_mapping)

        n = len(nums)
        count_zero = 0
        # print(index_updation_freq_mapping)
        for i in range(n):
            # print(nums[i] - index_updation_freq_mapping[i])
            if i in index_updation_freq_mapping:
                if nums[i] != 0:
                    nums[i] = nums[i] - index_updation_freq_mapping[i]
            if nums[i] == 0:
                count_zero += 1

        return count_zero == n


sol = Solution()

nums = [1,0,1]
queries = [[0,2]]
print(f" {nums = } | {queries = } | {sol.isZeroArray(nums, queries) = }")

nums = [4,3,2,1]
queries = [[1,3],[0,2]]
print(f" {nums = } | {queries = } | {sol.isZeroArray(nums, queries) = }")