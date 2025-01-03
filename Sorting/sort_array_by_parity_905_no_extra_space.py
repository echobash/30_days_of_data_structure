from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = n - 1
        left = 0

        while left < right:
            # If even no is in left, it is at correct place. Do nothing and just traverse ahead
            if nums[left] % 2 == 0:
                left += 1
            # If odd no is in right, it is at correct place. Do nothing and just traverse back
            elif nums[right] % 2 == 1:
                right -= 1
            # If even no is in right and odd no is in left, both of these are not at correct places. So swap both and move ahead left and move back right
            else:
                (nums[left],nums[right]) = (nums[right],nums[left])
                left += 1
                right -= 1
            print(left,right,nums[left],nums[right])
        return nums


solution = Solution()

nums = [3,1,2,4]
print(nums, solution.sortArrayByParity(nums))

nums = [1,2]
print(nums, solution.sortArrayByParity(nums))

nums = [2,2,3,1]
print(nums, solution.sortArrayByParity(nums))

nums = [0]
print(nums, solution.sortArrayByParity(nums))
