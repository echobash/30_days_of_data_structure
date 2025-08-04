from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result_set = set()
        for num in nums:
            result_set.add(num)
            result_set.add(int(str(num)[::-1]))
        return len(result_set)


sol = Solution()

nums = [1,13,10,12,31]
print(f"{nums = } {sol.countDistinctIntegers(nums) = }")

nums = [2,2,2]
print(f"{nums = } {sol.countDistinctIntegers(nums) = }")

nums = [10,20,1,2]
print(f"{nums = } {sol.countDistinctIntegers(nums) = }")
