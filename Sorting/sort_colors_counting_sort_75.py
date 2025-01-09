from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums_counter = Counter(nums)
        # 2:2,0:2,1:2
        for i in range(nums_counter[0]):
            nums[i] = 0

        for i in range(nums_counter[0], nums_counter[0] + nums_counter[1]):
            nums[i] = 1

        for i in range(nums_counter[0] + nums_counter[1], nums_counter[0] + nums_counter[1] + nums_counter[2]):
            nums[i] = 2
        return  nums


nums = [2,0,2,1,1,0]
solution = Solution()
print("Sorted array- ",solution.sortColors(nums))