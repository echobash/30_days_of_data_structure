from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # -----By Linear Traversal-------
        max_no = float('-inf')
        second_max_no = float('-inf')

        for i in range(len(nums)):
            if nums[i] >= max_no:
                second_max_no = max_no
                max_no = nums[i]
            elif nums[i] >= second_max_no:
                second_max_no = nums[i]

        return max_no * second_max_no - max_no - second_max_no + 1



sol = Solution()

nums = [3,4,5,2]
print(nums, sol.maxProduct(nums))


nums = [1,5,4,5]
print(nums, sol.maxProduct(nums))


nums = [3,7]
print(nums, sol.maxProduct(nums))

