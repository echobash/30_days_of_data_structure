from typing import List
from collections import defaultdict


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Initialise an array of same size as nums
        n = len(nums)
        result = [0] * n

        # For each query, keep updating the result
        # if say query = [li, ri], do result[l1] += -1 and result[r1+1] += 1 (To balance it)
        # Handle the edge case above that if r1 == n - 1, don't do result[r1+1]
        # Once all queries have been run on the result, find prefix sum array of result
        # Then add the two arrays and check if all the elements of the array are zero or not

        for query in queries:
            l1 = query[0]
            r1 = query[1]

            result[l1] += -1

            if r1 != n - 1:
                result[r1 + 1] += 1

        # print(result)
        # Find prefix sum array of result
        curr_sum = 0
        for i in range(n):
            curr_sum += result[i]
            result[i] = curr_sum

        # Addd the two arrays and check if all values are zero or negative.
        # We are taking negative here since as per the question we have to take subsets so we can ignore negative ones already
        zero_count = 0
        for i in range(n):
            result[i] += nums[i]
            if result[i] < 0:
                result[i] = 0
            if result[i] == 0:
                zero_count += 1
        return zero_count == n


sol = Solution()

nums = [1,0,1]
queries = [[0,2]]
print(f" {nums = } | {queries = } | {sol.isZeroArray(nums, queries) = }")

nums = [4,3,2,1]
queries = [[1,3],[0,2]]
print(f" {nums = } | {queries = } | {sol.isZeroArray(nums, queries) = }")