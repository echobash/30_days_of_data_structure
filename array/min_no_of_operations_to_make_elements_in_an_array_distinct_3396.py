from typing import List


class Solution:
    def check_has_duplicate(self, nums):
        return len(nums) != len(set(nums))
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while len(nums) > 0:
            if self.check_has_duplicate(nums):
                nums = nums[3:]
                count += 1
            else:
                break
        return count


sol = Solution()

nums = [1,2,3,4,2,3,3,5,7]
print(f"{nums = } {sol.minimumOperations(nums) = }")

nums = [4,5,6,4,4]
print(f"{nums = } {sol.minimumOperations(nums) = }")

nums = [6,7,8,9]
print(f"{nums = } {sol.minimumOperations(nums) = }")
