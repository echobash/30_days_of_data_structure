from typing import List
from itertools import permutations


# THis is extreme bruteforce solution. Will optimize when I'll study backtracking.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res_set = set()
        ans = []
        for data in permutations(nums):
            res_set.add(tuple(data))
        for tuples in res_set:
            ans.append(list(tuples))

        return ans


sol = Solution()

nums = [1,1,2]
print(f"{nums = }, {sol.permuteUnique(nums) = }")

nums = [1,2,3]
print(f"{nums = }, {sol.permuteUnique(nums) = }")

nums = [1,1,1]
print(f"{nums = }, {sol.permuteUnique(nums) = }")
