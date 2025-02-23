from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        equal_pairs = 0
        for i in range(n):
            for j in range(n):
                if nums[i] + nums[j] == target and i != j:
                    equal_pairs += 1
        return equal_pairs



sol = Solution()

nums = ["777","7","77","77"]
target = "7777"
print(f"{nums = }  {target = }  {sol.numOfPairs(nums, target) = }")

nums = ["123","4","12","34"]
target = "1234"
print(f"{nums = }  {target = }  {sol.numOfPairs(nums, target) = }")

nums = ["1","1","1"]
target = "11"
print(f"{nums = }  {target = }  {sol.numOfPairs(nums, target) = }")
