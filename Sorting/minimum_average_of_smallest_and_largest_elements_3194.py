from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Sort the given array
        nums = sorted(nums)
        # 5 4 2 3
        # 2 3 4 5
        # Swap adjacent elements and increment the loop by 2 i.e take 2 elements at a time and swap them
        for i in range(0,n-1,2):
            (nums[i],nums[i+1]) = (nums[i+1],nums[i])
        return nums



sol = Solution()

nums = [5,4,2,3]
print(nums, sol.numberGame(nums))


nums = [2,5]
print(nums, sol.numberGame(nums))


nums = [4,3,2,1]
print(nums, sol.numberGame(nums))

