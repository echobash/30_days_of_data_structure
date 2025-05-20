from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        for query in queries:
            start = query[0]
            end = query[1]

            for i in range(start, end + 1):
                if nums[i] != 0:
                    nums[i] -= 1

        return nums.count(0) == len(nums)


sol = Solution()

nums = [1,0,1]
queries = [[0,2]]
print(f" {nums = } | {queries = } | {sol.isZeroArray(nums, queries) = }")

nums = [4,3,2,1]
queries = [[1,3],[0,2]]
print(f" {nums = } | {queries = } | {sol.isZeroArray(nums, queries) = }")